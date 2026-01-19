#!/usr/bin/python3
def no_c(my_string):
    result = ''.join([car for car in my_string if car != "c"] and [car for car in my_string if car != "C"])
    return result
