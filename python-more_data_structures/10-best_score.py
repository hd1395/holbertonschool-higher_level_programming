#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None or len(a_dictionary) == 0:
        return None
    return list(a_dictionary.keys())[list(a_dictionary.values()).index(sorted(a_dictionary.values())[-1])]
