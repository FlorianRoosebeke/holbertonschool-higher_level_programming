#!/usr/bin/python3
def no_c(my_string):
    trsl = str.maketrans('C', 'c', 'C')
    result = my_string.translate(trsl)
    return result
