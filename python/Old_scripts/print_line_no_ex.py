#!/usr/bin/env python3

while True:
	fil = input("filename? ")
	try:
		with open(fil, 'r') as f:
			x = f.read()
	except:
		print("ERROR opening file:", fil)	
		continue
	break

while True:
	lineno = int(input("line number? ")) - 1
	filelist = x.split('\n')
	if lineno > len(filelist):
		print("Error, file has only" , len(filelist), " lines")
		continue
	break

print(filelist[lineno])
