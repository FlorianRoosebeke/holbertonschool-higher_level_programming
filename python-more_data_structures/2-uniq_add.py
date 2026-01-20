#!/usr/bin/python3
def uniq_add(my_list=[]):
    add_number = []
    for i in range(len(my_list)):
        if my_list[i] not in add_number:
            add_number.append(my_list[i])
    result = sum(add_number)
    return result
