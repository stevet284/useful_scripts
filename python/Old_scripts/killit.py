#!/usr/bin/env python3

import os 
import argparse
import subprocess

parser=argparse.ArgumentParser(description="A program to find what is using a port and kill the process")

parser.add_argument('port' , type=int , help="Port to check")

args=parser.parse_args()
port=args.port

print("Looking for: ", port)

found_pid = [] + str(subprocess.check_output("lsof -n -i4TCP:%d"% port , shell=True)).split()


print("found: ", found_pid)

