'''#!/usr/bin/python3
fuction to print string in uppercase


def uppercase(str):
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            s = chr(ord(s) - 32)
        print("{}".format(s), end="")
    print('')'''
    #!/usr/bin/python3
    def uppercase(str):
            for b in str:
                        if ord(b) >= ord('a') and ord(b) <= ord('z'):
                                        char = chr(ord(b) - 32)
                                                else:
                                                                char = b
                                                                        print("{:s}".format(char), end="")
                                                                            print('')
