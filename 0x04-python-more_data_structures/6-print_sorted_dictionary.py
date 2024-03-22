#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dict = sorted(a_dictionary.keys())
    for a in a_dict:
        print(a, ":", a_dictionary[a])
