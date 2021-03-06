#!/bin/env python

import subprocess
import json

def checkauth_and_groups(username, required_groups):

	print "Authenticating as %s and validating groups"% username

	try:
		found_groups = [] + subprocess.check_output("ssh %s@localhost groups"% username , shell=True).split()
		print "%s authenticated " % username
	except:
		print "authentication ERROR"
		exit(1)

	for g in required_groups:
		if g in found_groups:
			print "found group: %s"% g
			return(g)
	print "user %s is not in %s " % (username, required_groups)
	exit(1)

with open('auth.json', 'r') as jsnfile:
	cfg = json.load(jsnfile)

required_groups = cfg['config']['required_groups']

print "first user needs to be in %s"%required_groups

username=raw_input("user1")
found_groups=checkauth_and_groups(username, required_groups)
required_groups.remove(found_groups)

print "2nd user needs to be in %s"%required_groups

username=raw_input("user2")
found_groups=checkauth_and_groups(username, required_groups)

print "SUCCESS: Both users authenicated !!"
