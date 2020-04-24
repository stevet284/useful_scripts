#!/usr/bin/env python

import hashlib

saltstr='w<(^G<FF>/~#j^:5'
print saltstr.hex()

x = raw_input("something ?")
y = raw_input("something ?")

hash = hashlib.sha256(x + y + saltstr)

print hash.hexdigest()


