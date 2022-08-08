#!/usr/bin/env python
import requests

if __name__ == '__main__':
    payload = f'''<!DOCTYPE ProductEvent>
<ProductEvent Version='2.0'>
<EventID>000000</EventID>
<DeviceID>1</DeviceID>
<ServerID>1</ServerID>
<Date>07_06_2022</Date>
<Time>SOMETIME</Time>

<ProductEventType>PRODUCTTYPE</ProductEventType>
<PosSystemIdentifier>1</PosSystemIdentifier>
<Stage>STAGE</Stage>
<NonDepleting>NONDEPLETING</NonDepleting>

<Product>
    <ID>SOMEID</ID>
    <Name>SOMENAME</Name>
    <Qty>1</Qty>
    <UnitCost>1.5</UnitCost>
    <ItemTotal>1</ItemTotal>
</Product>

<SubTotal>2</SubTotal>
<Tax>1,00</Tax>
<Total>2,00</Total>
</ProductEvent>
    '''

    r = f'http://localhost:8083/instore/posXml?activity=IncomingXML&XMLData={payload}'


    response = requests.get(r)
    print(f'{response.status_code} | {response.content.decode("utf-8")}')
