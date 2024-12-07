import logging
import json
import sys

from PyPDF2 import PdfReader

# logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.getLogger(__name__)

IGNORED_FIELDS = [
    'ID',
    'Code',
    'Data File Descriptions',
    'Type',
    'Data File Description',
    'From',
    'Year',
    'To',
    'Extraction',
    'Extraction %',
    'Re-Used',
    'from DUA',
    'Access Method',
    'Disposition',
    'Reason',
    'DIRECT ACCESS',
    '100%'
    'Migrated',
    'NA',
    'cohort',
    'CONT'
]


def is_int(x: str) -> bool:
    try:
        int(x)
        return True
    except ValueError:
        return False


class PDFProcessor:
    SUMMARY_ROW_HEADERS = {
        'Organization Name': 'organization',
        'DUA Number': 'contractNumber',
        'Contract Start Date': 'contractStartDate',
        'Contract End Date': 'contractEndDate',
        'Requested Date': 'requestedDate',
        'Requester': 'requesterName',
        'Requester\'s Email': 'requesterEmail',
        'Expiration Date': 'expirationDate',
    }

    def __init__(self, file_object: str) -> None:
        self.reader = PdfReader(file_object)
        self.number_of_pages = len(self.reader.pages)

        self.pages = [self.reader.pages[x].extract_text()
                      for x in range(self.number_of_pages)]

        self.summary_rows = {'summaryRows': {}}
        self.dua_rows = {'duaRows': []}

    def __str__(self):
        return vars(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def process_dua(self):
        data = self.extract_relevant_data()
        self.get_dua_rows(data)

        log.debug(json.dumps(self.dua_rows, indent=4))
        log.debug(json.dumps(self.summary_rows, indent=4))

        return {
            'duaRows': self.dua_rows['duaRows'],
            'summaryRows': self.summary_rows['summaryRows']
        }

    def get_summary_rows(self, content_range: list):
        if content_range[0] not in self.summary_rows and 'Phone' not in content_range[0]:

            self.summary_rows['summaryRows'][self.SUMMARY_ROW_HEADERS[content_range[0]]] \
                = content_range[-1]

    def extract_relevant_data(self) -> dict:
        relevant_records = False
        relevant_data = {}
        current_record = 0

        for page in self.pages:
            lines = page.split('\n')

            for index, line in enumerate(lines):
                try:
                    if line in self.SUMMARY_ROW_HEADERS:
                        self.get_summary_rows([x for x in lines[index: index + 4]])

                except IndexError:
                    break

                # Get duaRows
                if 'Documents' in line:
                    relevant_records = False

                if 'Data File Descriptions' in line:
                    relevant_records = True

                if relevant_records:
                    if line in IGNORED_FIELDS:
                        continue

                    if is_int(line) and len(line) > 4:
                        pdf_row_id = int(line)
                        current_record = pdf_row_id

                        if current_record not in relevant_data.keys():
                            relevant_data[current_record] = []

                    else:
                        relevant_data[current_record].append(line)

        return relevant_data

    def get_dua_rows(self, r_data: dict) -> None:
        for dua_id, data in r_data.items():
            if data:
                pdf_row_ids = [x['pdfRowId'] for x in self.dua_rows['duaRows']]
                years = [int(x) for x in data if is_int(x)]
                from_year, to_year = [], []

                if years:
                    if len(years) == 2:
                        from_year.append(years[0])
                        to_year.append(years[1])

                    else:
                        for year in range(len(years)):
                            try:
                                from_year.append(years[year])
                                to_year.append(years[year + 1])

                            except IndexError:
                                break

                if not is_int(data[2]) and len(data) >= 4:
                    file_description = ''.join(data[1].split('-')[1:]) + data[2]
                else:
                    file_description = ''.join(data[1].split('-')[1:])

                if dua_id not in pdf_row_ids:
                    self.dua_rows['duaRows'].append({
                        'pdfRowId': dua_id,
                        'description': file_description.lstrip(' '),
                        'code': data[0],
                        'fromYear': from_year,
                        'toYear': to_year
                    })

                else:
                    for i in self.dua_rows['duaRows']:
                        if i['pdfRowId'] == dua_id:
                            i['fromYear'].append(min(years))
                            i['toYear'].append(max(years))


if __name__ == '__main__':
    with PDFProcessor('CONT200616108.pdf') as p:
        dua_data = p.process_dua()

        log.info(json.dumps(dua_data, indent=4))
