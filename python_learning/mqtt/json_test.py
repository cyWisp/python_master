import json

if __name__ == '__main__':
    test = {
        'person': {
            'name': 'rob',
            'age': 36
        },
        'car': {
            'make': 'ford',
            'model': 'mustang'
        }
    }

    print(type(json.dumps(test)))