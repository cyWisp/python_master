from enum import Enum
import json

class Payloads(Enum):
    ALL_PAYLOADS = {
        'BLINK_REQUEST_ALL_LEDS': json.dumps(
            {
                "header": {
                    "guid": "FF34556789993322112F345567899933",
                    "source": "0A:0B:0D:11:33:22",
                    "destination": "0A:0B:0D:11:22:33",
                    "correlationId": "FF34556789993322112F345567899933",
                    "dateTime": "2018-03-01T21:23:48+0000",
                    "versionInfo": {
                        "api": "3.x.x",
                        "applianceType": "FRYER-1.0.0",
                        "applianceSpec": "Sub1-1.x.x"
                    },
                    "type": "BLINK_REQUEST",
                    "equipmentType": "FRYER",
                    "equipmentManufacturer": "Company X",
                    "equipmentModel": "Model X",
                    "deviceType": "Controller",
                    "deviceManufacturer": "Kitchen Brains",
                    "deviceModel": "VTC-3000",
                    "siteId": 123,
                    "siteName": "Test Stratford",
                    "siteNumber": "123",
                    "lqi": 50
                },
                "time": 5,
                "all": False,
                "spec": "WIFI_LED;BT_LED;PWR_LED;DISPLAY"
            }
        ),
        'BLINK_REQUEST_SINGLE_LED': json.dumps(
            {
                "header": {
                    "guid": "FF34556789993322112F345567899933",
                    "source": "0A:0B:0D:11:33:22",
                    "destination": "0A:0B:0D:11:22:33",
                    "correlationId": "FF34556789993322112F345567899933",
                    "dateTime": "2018-03-01T21:23:48+0000",
                    "versionInfo": {
                        "api": "3.x.x",
                        "applianceType": "FRYER-1.0.0",
                        "applianceSpec": "Sub1-1.x.x"
                    },
                    "type": "BLINK_REQUEST",
                    "equipmentType": "FRYER",
                    "equipmentManufacturer": "Company X",
                    "equipmentModel": "Model X",
                    "deviceType": "Controller",
                    "deviceManufacturer": "Kitchen Brains",
                    "deviceModel": "VTC-3000",
                    "siteId": 123,
                    "siteName": "Test Stratford",
                    "siteNumber": "123",
                    "lqi": 50
                },
                "time": 5,
                "all": False,
                "spec": "WIFI_LED"
            }
        ),
        'BLINK_REQUEST_ALL_TRUE': json.dumps(
            {
                "header": {
                    "guid": "FF34556789993322112F345567899933",
                    "source": "0A:0B:0D:11:33:22",
                    "destination": "0A:0B:0D:11:22:33",
                    "correlationId": "FF34556789993322112F345567899933",
                    "dateTime": "2018-03-01T21:23:48+0000",
                    "versionInfo": {
                        "api": "3.x.x",
                        "applianceType": "FRYER-1.0.0",
                        "applianceSpec": "Sub1-1.x.x"
                    },
                    "type": "BLINK_REQUEST",
                    "equipmentType": "FRYER",
                    "equipmentManufacturer": "Company X",
                    "equipmentModel": "Model X",
                    "deviceType": "Controller",
                    "deviceManufacturer": "Kitchen Brains",
                    "deviceModel": "VTC-3000",
                    "siteId": 123,
                    "siteName": "Test Stratford",
                    "siteNumber": "123",
                    "lqi": 50
                },
                "time": 5,
                "all": True,
                "spec": "WIFI_LED;BT_LED;PWR_LED;DISPLAY"
            }
        )
    }