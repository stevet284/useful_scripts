#!/usr/bin/env python3

filename = input("filename ? ")

print("now enter something, press  when to finish ")

filestr=""

while True:
	x = input()
	if x == "":
		break
	filestr += x + "\n"
	

with open(filename, 'w') as f:
	f.write(filestr)
