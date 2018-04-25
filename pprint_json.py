import json
import argparse
import os.path
import sys


def load_json_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file:
        return json.load(file)


def parse_command_line_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'filename',
        help='a JSON file for pretty printing',
        type=str,
    )

    parser.add_argument(
        '-i',
        '--indent',
        help='indent level for pretty printing of both JSON array elements '
             'and object members',
        default=4,
        type=int,
    )

    command_line_arguments = parser.parse_args()

    return command_line_arguments


def main():
    command_line_arguments = parse_command_line_arguments()

    filename = command_line_arguments.filename
    indent_level = command_line_arguments.indent

    try:
        decoded_data = load_json_data(filename)
    except (UnicodeDecodeError, json.JSONDecodeError):
        sys.exit('JSON file has invalid format')

    if not decoded_data:
        sys.exit('JSON file not found')

    print(json.dumps(decoded_data, ensure_ascii=False, indent=indent_level))


if __name__ == '__main__':
    main()
