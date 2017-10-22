import json
import sys


def load_data(filepath):
    json_file = open(filepath, 'r')
    json_content = json_file.read()
    json_file.close()
    return json_content


def pretty_print_json(data):
    print(json.dumps(json.loads(data), indent=4, ensure_ascii=False))


if __name__ == '__main__':
    pretty_print_json(load_data(sys.argv[1]))
