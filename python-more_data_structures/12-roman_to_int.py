#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    converter = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    number_list = []
    for letter in roman_string:
        if converter[letter]:
            number_list.append(converter[letter])
    for i in range(len(number_list) - 1):
        if number_list[i + 1] and number_list[i + 1] > number_list[i]:
            number_list[i + 1] -= number_list[i]
            number_list[i] = 0
    return (sum(number_list))
