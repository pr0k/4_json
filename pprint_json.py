import json
from sys import argv

def load_data(filepath):
    with open(filepath, 'r') as json_file:
        return json.load(json_file)

def pretty_print_json(python_file):
    return json.dumps(python_file, ensure_ascii=False, indent=4, sort_keys=True)

if __name__ == '__main__':
        print(pretty_print_json(load_data(argv[1])))
