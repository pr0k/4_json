import json
from sys import argv

def load_data(filepath):
    with open(filepath, 'r') as json_data_file:
        return json.load(json_data_file)

def prettify_json(python_obj):
    return json.dumps(python_obj, ensure_ascii=False, indent=4, sort_keys=True)

if __name__ == '__main__':
    try:
        print(prettify_json(load_data(argv[1])))
    except IOError:
        print('file not found!\ntry again')
    except ValueError:
        print('there is no JSON data in the file!\nspecify the JSON data file')
    except IndexError:
        print('no path to file to be processed!\ntry $ python pprint_json.py <path to file>')
