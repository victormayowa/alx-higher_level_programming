#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = {}
        for key, value in a_dictionary.items():
            new_dictionary[key] = value * 2
        return new_dictionary
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
