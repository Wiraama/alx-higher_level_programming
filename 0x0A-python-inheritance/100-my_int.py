#!/usr/bin/python3
"""module"""


class MyInt(int):
    """ class ineherited from int"""

    def __init__(self, oper):
        self.oper = oper

    def __eq__(self, other):
        """inverts == operator"""
        return not self.oper == other

    def __ne__(self, other):
        """ inverts != operator"""
        return not self.oper != other
