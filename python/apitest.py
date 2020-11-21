#!/usr/bin/env python3

import argparse
import os
import requests
import argparse
import json
import pprint

parser=argparse.ArgumentParser()
parser.add_argument('--search' , help = 'movie id' , required=True)

args=parser.parse_args()

config_file = os.getcwd() + '/' + __file__.replace(".py",".json")

try:
  config = json.load(open(config_file))
except:
  print("error loading config", config_file)
  exit(1)

site = config.get("site")
api_key = config.get("api_key")
api_version = config.get("api_version")

page = 'search/movie'
searchstr = args.search
#url = site + '/' + api_version + '/' + page + '?' + 'api_key=' + api_key  + '&query=' + searchstr 
url = f"{site}/{api_version}/{page}?api_key={api_key}&query={searchstr}"

# + '&page=1'
print(url)
r = requests.get(url)

if r.status_code == 200:
  pprint.pprint(r.json())
#  print(type(r.text))
  movie_dict=json.loads(r.text)
elif r.status_code == 404:
  print("NOT FOUND")
elif r.status_code == 401:
  print("NOT AUTHORISED")
else:
  print("Some other error " + r.status_code)



