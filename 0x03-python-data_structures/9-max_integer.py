#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        k = my_list[0]
        for i in my_list:
            if i > k:
                k = i
        return k
