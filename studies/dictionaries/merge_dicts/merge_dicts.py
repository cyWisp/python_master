#!/usr/bin/env python

def merge(a, b):
    return {**a, **b}

def copy_merge(a, b):
    temp = a.copy()
    temp.update(b)
    return temp

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

if __name__ == '__main__':
    dict_1 = {
        "person_1": {
            "name": "rob",
            "age": 36
        },
        "person_2": {
            "name": "mike",
            "age": "22"
        }
    }

    dict_2 = {
        "person_1": {
            "name": "max",
            "age": "33"
        },
        "person_3": {
            "name": "bill",
            "age": "45"
        },
        "weird_entry": {
            "some_val": [
                "val_1",
                "val_2",
                "val_3"
            ],
            "another_dict": {
                "one": "1",
                "two": "2",
                "three": "3"
            }
        }
    }

    # merged = merge(dict_1, dict_2)
    # merged_2 = merge_dicts(dict_1, dict_2)
    # merged_3 = copy_merge(dict_1, dict_2)

    # print(merged)
    # print(merged_2)
    # print(merged_3)
