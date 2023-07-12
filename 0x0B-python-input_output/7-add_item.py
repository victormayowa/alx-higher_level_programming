#!/usr/bin/python3
'''
it combines the fuction of loading  and saving json files
'''
import sys
from os import path 
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file
'''
import all file from the pythone script
'''
filename = "add_item.json"
'''
# lets see
# Check if the file exists
'''
if path.exists(filename):
    # Load existing data from the file
    my_list = load_from_json_file(filename)
else:
    # Create an empty list
    my_list = []
# Add command-line arguments to the list
my_list.extend(sys.argv[1:])
# Save the updated list to the file
save_to_json_file(my_list, filename)
'''
save file in json format
'''
