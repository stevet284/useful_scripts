#!/bin/env /usr/bin/python

import random
import string
import argparse
import yaml

#def pw_gen(size ,chars=string.ascii_letters + string.digits + string.punctuation):
def pw_gen(size, skipchars=""):
	chars=string.ascii_letters + string.digits + string.punctuation
	#print skipchars
	for c in skipchars:
		chars = chars.replace(c, '')
	#print chars
	return ''.join(random.choice(chars) for _ in range(size))


###Main Program starts here###########

parser = argparse.ArgumentParser(description='Random Password Generator')

parser.add_argument('digits', action="store",  type=int, help='specify the number of digits')
parser.add_argument('--skipchars', action="store",  type=str, help='specify any chars to skip')

args=parser.parse_args()
config = yaml.load(open('random2.yaml'))

print config

if args.skipchars:
	skipchars = str(args.skipchars)  + str(config['variables']['skipchars'])
else:
	 skipchars = str(config['variables']['skipchars'])

print pw_gen(int(args.digits), skipchars)


