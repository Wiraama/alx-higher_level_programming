#!/usr/bin/python3

import sys

if __name__ == "__main__":

    def arguments():
        args_len = len(sys.argv) -1

        if args_len == 0:
            print("0 Arguments.")
        else:
            print("{} arguments:".format(args_len))
            for i, args in enumerate(sys.argv[1:], 1):
                print("{}: {}".format(i, args))

    arguments()
