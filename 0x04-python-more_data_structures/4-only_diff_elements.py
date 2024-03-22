#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    both_set = set_1 ^ set_2
    sorted(both_set)
    return both_set
