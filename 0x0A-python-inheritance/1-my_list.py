#!/usr/bin/python3
""" Write a class MyList that inheriits from list:"""


class MyList(list):
    """class of mylist"""

    def print_sorted(self):
        """ method instance to print list when sortedt"""

        list_sorted = sorted(self)
        print(list_sorted)
