#!/bin/env python3.6

mystr="i am a string"

mylist=["one", "two", "three"]

mytup=("one", "two", "three")

mydict={ "fred" : 1 , "joe": 19 }

print(f"mystr is ", type(mystr))
print(f"mylist is ", type(mylist))
print(f"mytup is ", type(mytup))
print(f"mydict is ", type(mydict))

for x in mystr:
	print(x)

for x in mylist:
	print(x.upper())

for x in mytup:
	print(x)

print(mydict.values())

dictlist=(list(mydict.values()))
for x in dictlist:
	print(x)


print("joe is ", mydict['joe'])


print(" mylist: ", mylist)
print(" mylist[1:] ", mylist[1:])
