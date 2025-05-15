#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    error = 0
    try:
        for i in range(x):
            print(my_list[i], end = "")
        print()
    except IndexError:
        i -= 1
    return i + 1
