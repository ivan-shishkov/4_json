# Prettify JSON

This script allows to execute pretty-print of JSON file content to console.

# Quickstart

For script's launching need to install Python 3.5.

Usage:

```bash

$ python3 pprint_json.py -h
usage: pprint_json.py [-h] [-i INDENT] [-s] filename

positional arguments:
  filename              a JSON file for pretty printing

optional arguments:
  -h, --help            show this help message and exit
  -i INDENT, --indent INDENT
                        indent level for pretty printing of both JSON array
                        elements and object members (default: 4)
  -s, --sort            if set, then the output of dictionaries will be sorted
                        by key

```

Example of script launch on Linux, Python 3.5:

```bash

$ python3 pprint_json.py <path to file>
# TODO add output example

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
