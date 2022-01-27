import json

template = {
    "header": {
        "versionInfo": {
            "api": "3.x.x",
            "applianceType": "FRYER-1.0.0",
            "applianceSpec": "Sub1-1.x.x"
        },
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
    }
}

myd = {
    "header": {
        'type': 'BLINK_REQUEST',
        'destination': 'NEW DESTINATION'
    },
    'time': 10,
    'all': 'true',
    'spec': 'WIFI_LED;BT_LED;PWR_LED;DISPLAY'
}


def merge_dicts(a, b, path=None):
    """allows you to merge into one two dictionaries with nested dictionaries"""
    if path is None:
        path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge_dicts(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass
            else:
                raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
        else:
            a[key] = b[key]
    return a


def merg(a, b):
    return {**a, **b}

def copy_merge(a, b):
    temp = a.copy()
    temp.update(b)
    return temp

def merge_3(a, b):
    for key, val in a.items():
        if isinstance(val, dict):

print("** **")
print(json.dumps(merg(myd, template), indent=4))
print("func")
print(json.dumps(merge_dicts(myd, template), indent=4))
print("*******")
print(json.dumps(copy_merge(myd, template), indent=4))
