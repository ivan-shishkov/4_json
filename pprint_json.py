import json
import argparse


def load_data(filepath):
    pass


def pretty_print_json(data):
    pass


def parse_command_line_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'filename',
        help='a JSON file for pretty printing',
        type=str,
    )

    command_line_arguments = parser.parse_args()

    return command_line_arguments


def main():
    command_line_arguments = parse_command_line_arguments()

    filename = command_line_arguments.filename


if __name__ == '__main__':
    main()
