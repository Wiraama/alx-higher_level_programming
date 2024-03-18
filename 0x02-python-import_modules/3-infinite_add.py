#!/usr/bin/python3
""" prints results of additaional argments received """

if __name__ == "__main__":
    import sys

    result = 0
    if sys.argv == 0:
        print("0")
    for n in sys.argv[1:]:
        result += int(n)
        
    print(result)
