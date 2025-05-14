#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    max_value = sorted(a_dictionary.values())[-1]
    key_index = list(a_dictionary.values()).index(max_value)
    return list(a_dictionary.keys())[key_index]
