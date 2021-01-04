#!/usr/bin/python3
import subprocess , sys, re

from subprocess import Popen, PIPE

cmd=["rpm" , "-qip" , "/root/useful_scripts/rpmbuild/RPMS/x86_64/utils-1.0.0-1.x86_64.rpm"]

def sig(rpm):
  cmd=["rpm" , "-qip" , rpm]
  with Popen(cmd, stdout=PIPE, universal_newlines=True) as process:
    for line in process.stdout:
      x = re.match("^Signature   : .*", line)
      if x:
        return(x.group(0).replace("Signature   : ", ""))

sigy = sig("/root/useful_scripts/rpmbuild/RPMS/x86_64/utils-1.0.0-1.x86_64.rpm")

print("sig = ", sigy)

