#!/usr/bin/python3
def best_score(a_dictionary):
    highest = None
    best = None
    for key, value in a_dictionary.items():
        current = max(value)
        if highest is None or current > highest:
            highest = current
            best = key
    return best, highest
