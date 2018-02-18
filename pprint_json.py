import json
from sys import argv

# Decodes not formatted json data into python data
def decode_json_data(filepath):
    with open(filepath, 'r') as json_data_file:
        return json.load(json_data_file)

# Encodes python data into a pretty JSON format
def encode_python_data(python_data_file):
    return json.dumps(python_data_file, ensure_ascii=False, indent=4, sort_keys=True)

if __name__ == '__main__':
    try:
        print(encode_python_data(decode_json_data(argv[1])))
    except IOError:
        print('file not found!\ntry again')
    except ValueError:
        print('there is no JSON data in the file!\nspecify the JSON data file')
    except IndexError:
        print('no path to file to be processed!\ntry $ python pprint_json.py <path to file>')
