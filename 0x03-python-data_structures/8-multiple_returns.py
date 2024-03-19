#!/usr/bin/python3
def multiple_returns(sentence):
    t = ()
    count = 0
    if sentence == 0:
        t = (0, "None")

    else:
        count = len(sentence)
        first = sentence[0]
        t = (count, first)
    return t
