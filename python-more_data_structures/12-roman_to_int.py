#!/usr/bin/python3
def roman_to_int(roman_string):
    r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500}
    conv = []
    for n in roman_string:
        conv.append(r[n])
    for i in range(1, len(conv)):
        if conv[i] > conv[i-1]:
            conv[i-1] *= -1
    return sum(conv)
