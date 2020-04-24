#!/bin/env python3.6

from time import gmtime

x=gmtime()
year=x.tm_year


name=input("what is your name?")

age=input("what is your age ?")
count=int(input("count?"))

agediff = 100 - int(age)

when100 = year + agediff

for y in range(1, count):
	print(name, " you will be 100 in ", when100, end=" ")


