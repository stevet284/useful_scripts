

import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("url", help="give me a url inc http:// or  https://")
parser.add_argument("filename", help="give me a file to write to")
args = parser.parse_args()
myurl = args.url
file = args.filename

r = requests.get(myurl)

print("status = " , r.status_code)

print(r)
