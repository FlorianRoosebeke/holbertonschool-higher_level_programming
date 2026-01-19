#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    value_max = my_list[0]
    for i in my_list:
        if i > value_max:
            value_max = i
    return value_max 
