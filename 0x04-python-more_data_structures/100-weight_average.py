#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    i = 0
    t = 0
    sum = 0
    for t in range(len(my_list)):
        sum += my_list[t][0] * my_list[t][1]
        i += my_list[t][1]
    return sum / i
