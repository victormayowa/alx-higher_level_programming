#!/usr/bin/python3
'''it combines the fuction of loading  and saving json files '''

import sys
from os import path 
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file
'''
import all file from the pythone script
'''

filename = "add_item.json"
'''
# lets see
# Check if the file exists
'''

if path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []
my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
''' save file in json format '''
