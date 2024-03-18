#!/usr/bin/python3
""" Write a program that prints all the names defined by the compiled module hidden_4.pyc"""


if __name__ == "__main__":
    import hidden_4

    name = dir(hidden_4)
    for n in name:
        if n[:2] != "__":
            print(n)
