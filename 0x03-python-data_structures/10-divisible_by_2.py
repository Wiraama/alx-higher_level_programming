#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for num in my_list:
        number = num % 2
        if number == 0:
            return True
        else:
            return False
