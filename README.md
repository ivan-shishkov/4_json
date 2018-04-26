# Prettify JSON

This script allows to execute pretty-print of JSON file content to console.

# Quickstart

For script launch need to install Python 3.5.

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

Example of script launch on Linux:

```bash

$ python3 pprint_json.py shops.json --sort
[
    {
        "Cells": {
            "Address": "Krasnaya street 29",
            "IsNetObject": "yes",
            "Name": "Aroma World",
            "OperatingCompany": "Aroma World",
            "PublicPhone": [
                {
                    "PublicPhone": "(123) 123-45-67"
                }
            ],
            "TypeService": "sale of food products",
            "geoData": {
                "coordinates": [
                    12.345678,
                    22.334455
                ],
                "type": "Point"
            },
            "global_id": 14371450
        },
        "Id": "79742784-9ef3-4543-bc98-a219a8903c18",
        "Number": 1
    },
    {
        "Cells": {
            "Address": "Svetlaya street 12",
            "IsNetObject": "yes",
            "Name": "My SuperShop",
            "OperatingCompany": "SuperShop",
            "PublicPhone": [
                {
                    "PublicPhone": "(123) 987-65-43"
                }
            ],
            "TypeService": "sale of food products",
            "geoData": {
                "coordinates": [
                    55.443322,
                    11.223344
                ],
                "type": "Point"
            },
            "global_id": 14934782
        },
        "Id": "1bd07c21-05de-4015-b015-d22657168ded",
        "Number": 2
    }
]


```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
