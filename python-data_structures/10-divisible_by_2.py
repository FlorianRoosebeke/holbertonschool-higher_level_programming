#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = my_list.copy()

    for i in range(len(result)):
        result[i] = (result[i] % 2 == 0)
    return result
