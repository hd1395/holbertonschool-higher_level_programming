#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic_keys = sorted(a_dictionary.keys())
    for key in dic_keys:
        print("{0}: {1}".format(key, a_dictionary[key]))
