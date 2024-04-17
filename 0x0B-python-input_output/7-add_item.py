#!/usr/bin/python3
"""
This script adds all arguments to a Python list and saves them to a file.
"""

import sys
import os.path
from json import dumps
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# File to store the list
file_name = "add_item.json"

# Initialize an empty list or load the existing list
if path.exists(file_name):
    items = load_from_json_file(file_name)
else:
    items = []

# Add command line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, file_name)
