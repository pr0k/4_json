import json
from sys import argv

def load_data(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def pretty_print_json(data):
    return json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True)

if __name__ == '__main__':
        print(pretty_print_json(load_data(argv[1])))
