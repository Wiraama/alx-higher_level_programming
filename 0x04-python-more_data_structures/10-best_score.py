#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    highest = None
    best = None
    for key, value in a_dictionary.items():

        if highest is None or value > highest:
            highest = value
            best = key
    return best
