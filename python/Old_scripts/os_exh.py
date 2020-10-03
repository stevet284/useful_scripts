#!/usr/bin/env python2

from math import pi
import os

digits = os.getenv("DIGITS", "10")
digits = int(digits)


print("%.*f" % (digits, pi))
