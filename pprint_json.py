import json
import sys


def load_data(filepath):
    f = open(filepath, 'r')
    data = f.read()
    f.close()
    return data


def pretty_print_json(data):
    print(json.dumps(json.loads(data), indent=4, ensure_ascii=False))


if __name__ == '__main__':
    pretty_print_json(load_data(sys.argv[1]))
