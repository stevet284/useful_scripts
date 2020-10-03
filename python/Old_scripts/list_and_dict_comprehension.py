#!/bin/env python3

list1 = ['joe' , 'alfie' , 'lucy' , 'zadar' ,  'cookie' ,  'rrinocoooo' , 'orinocoooo' , 'heidi']


name=str(input("name to check?")).lower()

#for l in list1:
#	dict1.update({l : len(l)})

dict1={ f : len(f) for f in list1 }

lenlist=sorted(dict1.values(), reverse=True)
print(lenlist)

long=lenlist[0]
print(long ,  " is the longest")
print(lenlist[-1],  " is the shorteds")

for k, v in dict1.items():
	if v == long:
		print(k)

print("new#################")
print(dict1.items())
print(dict1.keys())
print(dict1.values())

newdict={k : v  for k,v in dict1.items() if v==long}

longestl=[x for x in newdict.keys()]
st=""

# Convert a list to a string

st = ''.join([ "%s \n" % ((' ').join( longestl ) )]) 

print("longest = ", st)

