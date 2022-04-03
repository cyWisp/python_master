#!/usr/bin/env python
import re
import logging
import xmltodict

LOG_FILE = 'catalina.2021-11-23.log'

EXAMPLE = '''<ProductEvent xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" Version="2.0">
  <EventID>3145760</EventID>
  <DeviceID>3</DeviceID>
  <ServerID>614</ServerID>
  <Date>2021-11-23</Date>
  <Time>12:40:37:05401</Time>
  <ProductEventType>Sold</ProductEventType>
  <PosSystemIdentifier>1</PosSystemIdentifier>
  <Stage>ORDER_TAKEN</Stage>
  <Product>
    <ID>300017</ID>
    <Name>2xPommes Gr Dip</Name>
    <Qty>1</Qty>
  </Product>
  <Product>
    <ID>297050</ID>
    <Name>Ketchup Dip</Name>
    <Qty>1</Qty>
  </Product>
  <Product>
    <ID>297060</ID>
    <Name>Pommes Sau Dip</Name>
    <Qty>1</Qty>
  </Product>
  <Product>
    <ID>170031</ID>
    <Name>4 Crispy</Name>
    <Qty>1</Qty>
  </Product>
  <Product>
    <ID>160050</ID>
    <Name>6 Hot Wings</Name>
    <Qty>1</Qty>
  </Product>
  <Product>
    <ID>180180</ID>
    <Name>4 Filet Bite</Name>
    <Qty>1</Qty>
  </Product>
  <Product>
    <ID>680020</ID>
    <Name>Uptrade Bucket</Name>
    <Qty>1</Qty>
  </Product>
  <Product>
    <ID>400460</ID>
    <Name>Cheese Crunch</Name>
    <Qty>1</Qty>
  </Product>
  <Product>
    <ID>400460</ID>
    <Name>Cheese Crunch</Name>
    <Qty>1</Qty>
  </Product>
  <SubTotal>12,14</SubTotal>
  <Tax>0,85</Tax>
  <Total>12,99</Total>
</ProductEvent>
'''

reg_date = re.compile(r'([A-Z][a-z]{2}) (\d{2},) (\d{4}) (\d{1,2}:\d{2}:\d{2}) ([A-Z]{2})')

def get_log_file_contents(log_file):
    try:
        with open(log_file, 'r') as lf:
            return [line.replace('\n', '').lstrip(' ') for line in lf.readlines()]
    except (IOError, FileNotFoundError, Exception) as e:
        logging.exception(e)


if __name__ == '__main__':
    content = get_log_file_contents(LOG_FILE)

    records = list()

    new_record = ''

    for line in content:
        if line.startswith('<') and line.endswith('>'):
            if 'ResponseMsg' in line:
                continue
            else:
                if line == '</ProductEvent>':
                    new_record += line
                    records.append(new_record)
                    new_record = ''
                else:
                    new_record += line

    print(len(records))

    event_dict = xmltodict.parse(EXAMPLE)
    # print(event_dict)

    record = {k: event_dict[k] for k in event_dict}
    for k, v in record.items():
        print(f'{k}: {v}')



    # for r in records:
    #     print(r + '\n')




