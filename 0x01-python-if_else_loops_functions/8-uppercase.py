#!/usr/bin/python3
def uppercase(str):
    temp = list(str)
    for i in range(len(temp)):
        if temp[i] >= 'a' and temp[i] <= 'z':
            temp[i] = chr(ord(temp[i]) - 32)
    print("{}".format("".join(temp)))
