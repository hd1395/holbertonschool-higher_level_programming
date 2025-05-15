#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    result = 0
    subtractives = {"IV":4, "IX":9, "XL":40, "XC":90,
                    "CD":400, "CM":900}
    while len(roman_string) > 0:
        if roman_string[0:2] in list(subtractives.keys()):
            result += subtractives[roman_string[0:2]]
            roman_string = roman_string[2:]
        else:
            if roman_string[0:1] == 'I':
                result += 1
            elif roman_string[0:1] == 'V':
                result += 5
            elif roman_string[0:1] == 'X':
                result += 10
            elif roman_string[0:1] == 'L':
                result += 50
            elif roman_string[0:1] == 'C':
                result += 100
            elif roman_string[0:1] == 'D':
                result += 500
            elif roman_string[0:1] == 'M':
                result += 1000
            else:
                print("Error")
            roman_string = roman_string[1:]
    return result
