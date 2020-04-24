#!/usr/bin/env python3

def printlots(name, num):
	x=1
	while x <= num:
		print(name)
		x+=1



name = input("what is your name? ")
num = input("how may times to you want? ").strip()
if not num:
	num=1

printlots(name, int(num))
