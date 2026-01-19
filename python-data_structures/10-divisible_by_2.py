#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if new_list[i] % 2 == 0:
            return True
        else:
            return False
