#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == None:
        return None
    if sentence == "": return (tuple((0), None))
    return tuple((len(sentence), sentence[0]))
