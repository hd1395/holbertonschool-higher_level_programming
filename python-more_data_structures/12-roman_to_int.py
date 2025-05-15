#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    result = 0
    subtractives = {"IV": 4, "IX": 9, "XL": 40, "XC": 90,
                    "CD": 400, "CM": 900}
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
    while len(roman_string) > 0:
        if roman_string[0:2] in list(subtractives.keys()):
            result += subtractives[roman_string[0:2]]
            roman_string = roman_string[2:]
        else:
            result += values[roman_string[0:1]]
            roman_string = roman_string[1:]
    return result 
