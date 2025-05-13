#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    try:
        a1 = tuple_a[0]
    except IndexError:
        a1 = 0
    try:
        a2 = tuple_a[1]
    except IndexError:
        a2 = 0
    try:
        b1 = tuple_b[0]
    except IndexError:
        b1 = 0
    try:
        b2 = tuple_b[1]
    except IndexError:
        b2 = 0
    return (a1 + b1, a2 + b2)
