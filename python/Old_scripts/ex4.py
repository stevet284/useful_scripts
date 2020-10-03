#!/bin/env python3.6

num=int(input("number ?"))
max=num -1

results=[]
for x in range(2, max):
	if num % x == 0:
		results+=[x]

print(results)

if len(results) == 0:
	print(num , " is a prime number")

