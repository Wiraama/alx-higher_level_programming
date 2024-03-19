#!/usr/bin/python3
def multiple_returns(sentence):
    count = 0
    if sentence == 0:
        first = None
        return count, first

    count = len(sentence)
    first = sentence[0]
    return count, first
