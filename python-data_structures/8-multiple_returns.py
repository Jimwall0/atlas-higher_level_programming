#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence or sentence == None:
        return tuple((0, None))
    return tuple((len(sentence), sentence[0]))
