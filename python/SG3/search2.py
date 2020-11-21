#!/bin/env python
import re , json , os

#config_file = os.getcwd() + '/' + __file__.replace(".py",".json")
config_file = "./config.json"


#try:
config = json.load(open(config_file))
#except:
 # print("error loading config", config_file)
 # exit(1)

DBdir = config["config"]["DBdir"]
print DBdir

uuid="FF09AF73-429D-4CEA-853B-30239279FE2A"

translated_matches=[]
matched_lines=[]
with (open("./audit.log", 'r')) as f:
	for line in f.readlines():
#		print line
		if re.search(uuid, line):
			print "match !!"
			matched_lines.append(line)
			for code, text in config["SGmessages"].iteritems():
				print "%s %s" % ( code, text )
				line = line.replace(code, text)
			translated_matches.append(line)
			

for line in translated_matches:
	print line




