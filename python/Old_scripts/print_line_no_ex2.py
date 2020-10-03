#!/usr/bin/env python3

import argparse

parser=argparse.ArgumentParser()
parser.add_argument('file_name' , help = 'file to read')
parser.add_argument('lineno' , help = 'line number to print')

args=parser.parse_args()

try:
	with open(args.filename , 'r') as f
except:
	print("ERROR
	

#print(filelist[lineno])
