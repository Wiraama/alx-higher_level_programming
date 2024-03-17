#!/usr/bin/python3

if __name__ == "__main__":
    """..."""
    import sys

    args_len = len(sys.argv) -1

    if args_len == 0:
        print("0 Arguments.")
    elif args_len == 1:
        print("1 argument")
    else:
        print("{} arguments:".format(args_len))
    for i, args in enumerate(sys.argv[1:], 1):
        print("{}: {}".format(i, args))
