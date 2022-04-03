import logging
import os
import pandas as pd
import xmltodict
import xlsxwriter
import datetime
import collections
import re
import math

# define pandas output format
pd.options.display.max_rows = 500
pd.options.display.max_columns = 500
pd.options.display.width = 1000
pd.options.display.max_colwidth = 500

DEFAULT_REPORT_NAME = 'POS_XML_API_report_%Y-%m-%d_%H-%M-%S.xlsx'

# init logger as log
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(funcName)s - %(threadName)s - %(levelname)s - %(message)s',
                    handlers=[
                        # logging.FileHandler(log_file_name),
                        logging.StreamHandler()
                    ])
log = logging.getLogger()


def get_time_stamp_object(p_time_object):
    try:
        dt_object = datetime.datetime.strptime(p_time_object, '%b %d, %Y %I:%M:%S %p')
        dt_string = dt_object.strftime('%Y-%m-%d %H:%M:%S')

        dt_formatted = datetime.datetime.strptime(dt_string, '%Y-%m-%d %H:%M:%S')

        return dt_formatted, dt_string
    except (ValueError, Exception) as e:
        log.debug(f'Not a valid date time: {e}')


def get_log_time_stamp(time_stamp_str):
    for tod in ['AM', 'PM']:
        if tod in time_stamp_str:
            try:
                time_stamp = time_stamp_str[:time_stamp_str.find(tod)] + tod
                return get_time_stamp_object(str(time_stamp))
            except IndexError as e:
                log.exception(f'Timestamp not found: {e}')

def get_time_delta(time_stamp, event_date, event_time):
    try:
        t = event_time.split('.')[0] if '.' in event_time else ':'.join(event_time.split(':')[:-1])
        event_dt = datetime.datetime.strptime(' '.join([event_date, t]), '%Y-%m-%d %H:%M:%S')

        if time_stamp > event_dt:
            diff_token, diff = '+', time_stamp - event_dt
        else:
            diff_token, diff = '-', event_dt - time_stamp

        hours = math.floor(diff.seconds / 60 / 60)
        # Round down to the nearest whole second if greater than 1
        minutes = math.floor(diff.seconds / 60) if (diff.seconds / 60) > 1 else 00
        seconds = diff.seconds % 60

        return f'{diff_token}{hours:02d}:{minutes:02d}:{seconds:02d}'
    except (ValueError, Exception) as e:
        log.exception(f'Not a valid datetime object: {e}')


def get_log_file_contents(log_file):
    try:
        with open(log_file, 'r') as lf:
            return lf.readlines()
    except (IOError, FileNotFoundError, Exception) as e:
        log.exception(e)


def add_missing_product_columns(product_record):
    # Checks for missing items in product records and populates
    # them with empty strings
    for k in ['ID', 'Name', 'Qty', 'Currency', 'UnitCost', 'ItemTotal', 'ServerID']:
        if k not in product_record or product_record[k] is None:
            product_record[k] = ''

    # convert all records to Ordered Dict
    # Guarantees all product records are read the same way
    od = collections.OrderedDict(product_record)

    return od


def append_column_data(record, event_dict, time_stamp):
    # Get time stamp and time delta
    time_stamp_object, dt_string = get_log_time_stamp(time_stamp)
    time_delta = get_time_delta(time_stamp_object, record['Date'], record['Time'])

    # Set empty string as value for @Version column if not found
    if '@Version' not in record:
        record['@Version'] = ''

    if 'Product' in event_dict:
        if isinstance(event_dict['Product'], list):
            for product in event_dict['Product']:
                missing_columns = add_missing_product_columns(product)
                _ = record.copy()
                _.update(missing_columns)

                # Add CheckReceivedTimestamp and TimeDelta
                _['CheckReceivedTimestamp'], _['TimeDelta'] = dt_string, time_delta

                return _
        else:
            missing_columns = add_missing_product_columns(event_dict['Product'])
            missing_columns['CheckReceivedTimestamp'], missing_columns['TimeDelta'] = dt_string, time_delta
            record.update(missing_columns)
            return record
    else:
        # leave fields empty if product not passed to keep the transaction
        missing_columns = add_missing_product_columns({})
        missing_columns['CheckReceivedTimestamp'], missing_columns['TimeDelta'] = dt_string, time_delta
        record.update(missing_columns)

        return record


def remove_bad_chars(xml_event_str):
    return re.sub(r'\n\t\s+', '', xml_event_str)


def get_catalina_pos_api_events(log_file):
    log_file_content = get_log_file_contents(log_file)
    exclude_keys = ['Product']
    records = list()
    new_record, time_stamp, get_record = '', '', False

    for index, line in enumerate(log_file_content):
        try:
            # Parse XML records occuring witin a single line
            if '<ProductEvent ' in line and line.startswith('INFO'):
                time_stamp = log_file_content[index - 1]

                # Build event string from line beginning with '<ProductEvent'
                event_str = remove_bad_chars(line[line.find('<ProductEvent '):])

                event_dict = xmltodict.parse(event_str)['ProductEvent']

                record = {k: event_dict[k] for k in event_dict if k not in exclude_keys}

                r = append_column_data(record, event_dict, time_stamp)
                records.append(r)

            # Parse XML records occuring spanning multiple lines
            # Start multiline record
            if line.startswith('<ProductEvent '):
                time_stamp = log_file_content[index - 2]

                get_record = True

                new_record += '<ProductEvent>'
                continue

            # If get_record indicator is true, continue to append
            # to the new record
            if get_record:
                new_record += line

            # If end of record is detected, reset get_record indicator,
            # process and append new record to records list()
            if line.replace('\n', '') == '</ProductEvent>':
                get_record = False

                new_record = remove_bad_chars(new_record)

                event_dict = xmltodict.parse(new_record)['ProductEvent']

                record = {k: event_dict[k] for k in event_dict if k not in exclude_keys}

                r = append_column_data(record, event_dict, time_stamp)

                # Exclude duplicate records
                if r not in records:
                    records.append(r)

                # Reset default values
                new_record, time_stamp, event_dict = '', '', None
        except Exception as e:
            log.exception('Something went wrong: '.format(str(e)))

    if records:
        return records
    else:
        log.debug('No records found.')
        return None


def records_to_df(records):
    df = pd.DataFrame(records)

    # Explicitly insert columns that do not comprise a product record

    # Ensure that EventID is always in the first column
    event_id = df.pop('EventID')
    df.insert(0, 'EventID', event_id)

    version = df.pop('@Version')
    df.insert(1, 'Version', version)

    device_id = df.pop('DeviceID')
    df.insert(2, 'DeviceID', device_id)

    # Presence of this column differs between data sets - will show empty values if not provided
    server_id = df.pop('ServerID')
    df.insert(3, 'ServerID', server_id)

    # Create CheckTimestamp column and drop Date and Time columns
    date_time = (df['Date'].map(str) + ' ' + df['Time']).str[:22]
    df.insert(4, 'CheckTimestamp', date_time)
    df['CheckTimestamp'] = df['Date'].map(str) + ' ' + df['Time']

    df['CheckTimestamp'] = df['CheckTimestamp'].str[:19]
    df.drop(['Date', 'Time'], axis=1, inplace=True)

    # Insert CheckReceivedTimestamp and TimeDelta columns
    post_date_time = df.pop('CheckReceivedTimestamp')
    df.insert(5, 'CheckReceivedTimestamp', post_date_time)

    time_delta = df.pop('TimeDelta')
    df.insert(6, 'TimeDelta', time_delta)

    return df


def df_to_excel_sheet(df, writer, sheet_name='catalina'):
    height, width = df.shape
    df.to_excel(writer, sheet_name=sheet_name, index=False)

    workbook = writer.book
    worksheet = writer.sheets[sheet_name]

    # add autofilter
    worksheet.autofilter(0, 0, height, width - 1)

    # fancy coloring
    current_color = 'Dark'

    def format_row(r, color=current_color):
        formats = {
            'Dark': workbook.add_format({'bg_color': '#E5F8F3', 'border_color': '#BFBFBF', 'border': 1}),
            'Light': workbook.add_format({'bg_color': '#C7EDE0', 'border_color': '#BFBFBF', 'border': 1})
        }

        for col in range(0, width):
            worksheet.write(r, col, df.iloc[r - 1, col], formats[color])

    for row in range(1, height + 1):
        try:
            if df.iloc[row - 1, 0] != df.iloc[row - 2, 0]:
                current_color = 'Light' if current_color == 'Dark' else 'Dark'
            format_row(row, current_color)
        except (KeyError, IndexError, Exception) as e:
            log.exception(f'Error on row {row}: {e}')

    # auto width columns
    auto_filter_width = 4  # make it wider for autofilter ddl button
    for column in df:
        column_length = max(df[column].astype(str).map(len).max(), len(column))
        column_length += auto_filter_width
        col_idx = df.columns.get_loc(column)
        worksheet.set_column(col_idx, col_idx, column_length)


def parse_files(log_files, excel_out=None):
    # verify input files
    if isinstance(log_files, str):
        log.debug(f'single file received: {log_files}')
        log_files = [log_files]
    elif isinstance(log_files, list):
        log.debug(f'List of files received: {log_files}')
    else:
        raise TypeError(f'String or list expected. Type received: {type(log_files)}')

    # Create generated directory for results
    os.makedirs('generated', exist_ok=True)

    # create a list of the provided log files
    log.info(f'source log files: {[str(name) for name in log_files]}')

    # Create output file name
    if excel_out is None or DEFAULT_REPORT_NAME:
        excel_out = 'POS_API_report_' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.xlsx'
    log.info(f'target file name: {excel_out}')

    # do not fill the execution path with trash
    excel_out = 'generated/' + excel_out

    with pd.ExcelWriter(path=excel_out, engine='xlsxwriter', datetime_format='mmm d yyy hh:mm:ss') as writer:
        for log_file in log_files:
            try:
                log.debug(f'Processing file: {log_file} ...')

                # major execution diversion -> get_catalina_pos_api_events
                # skip file if no ProductEvent records found
                log_records = get_catalina_pos_api_events(log_file=log_file)

                if log_records:
                    # convert records to data frame
                    log_records_df = records_to_df(records=log_records)

                    # write records to excel spread sheet
                    df_to_excel_sheet(df=log_records_df, writer=writer, sheet_name=os.path.basename(log_file))
                    log.debug(f'Successfully processed the file: {log_file}')

            except Exception as e:
                log.error(f'failed to process {log_file}: {e}')

    if excel_out:
        log.debug(f'the size of excel_out is {os.path.getsize(excel_out)}')
        log.debug(f'excel_out to return: {excel_out}')

    # Excel out is the file path to be passed to flask app
    return excel_out


if __name__ == '__main__':
    import configargparse

    parser = configargparse.get_argument_parser(name='default')
    parser.add_argument('-l', '--log-level', type=str, env_var='LOG_LEVEL', default='INFO', help='default: %(default)s')
    parser.add_argument('-c', '--catalina-log', required=True, type=str, env_var='CATALINA_LOG', nargs='+',
                        help='scktomcat\'s catalina log file. can take multiple files')
    parser.add_argument('-e', '--excel-file', type=str, env_var='EXCEL_FILE',
                        default=DEFAULT_REPORT_NAME,
                        help='Excel xslx file to output results. default: %(default)s')

    cfg, _ = parser.parse_known_args()

    # change log level if needed
    if log.getEffectiveLevel() != cfg.log_level:
        log.setLevel(cfg.log_level)

    parse_files(log_files=cfg.catalina_log, excel_out=cfg.excel_file)
