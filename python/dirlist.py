#!/usr/bin/python3

import os

dirlist = os.listdir(".")

print(dirlist)


f = open("test.txt" , "r")
x = f.read()


print(x)

f.close()
