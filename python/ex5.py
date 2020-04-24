#!/bin/env python3.6

def poplist( alist ):
	for m in range(random.randint(1,100)):
	  	alist+=[random.randint(1,100)]
	return 0

import random

a = []
b = []

poplist(a)
poplist(b)

print(sorted(a))
print(sorted(b))

c = []

for x in a:
	if x in b and x not in c:
		c+=[x]

print(c)

