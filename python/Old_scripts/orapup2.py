#!/bin/env python

"""
Creates a yaml file for puppet.
takes CSV with the following format:

svc_node,volume,q_tree,mount,options,owner

if the owner contains oracle the mount is created oracle:orainst 0770
if the owner contains asm the mount is created oragrid:admdata 0775
"""

####function do create a list of subdirs##########
def child_mounts(mount, mount_list):
  lastmount=""
  new_list=[]
  pathlist=mount.split("/")
  for dir in pathlist:
   if dir == '':
    continue
   newmount = lastmount + "/" + dir
   if ( newmount not in mount_list ) and ( newmount not in new_list ):
     #print "adding : %s" % newmount
     new_list += [newmount]
   lastmount = newmount
  return(new_list)

###########Main Program####################
import csv

asm_mounts=[]
ora_mounts=[]

line=1
with open('ora.csv') as csvfile:
 orareader = csv.reader(csvfile)
 for row in orareader:
  lenrow = len(row)
  if lenrow < 7:
    print "ERROR: line %s the csv needs at least 7 columns" % line
    exit(1)
  
  svc_node=row[0]
  vol=row[1]
  qtree=row[2]
  mount=row[3]
  owner=row[4]
  group=row[5]
  perms=row[6]
  label=vol
  
  print
  print "\nmounts:"
  if qtree:
   vol += ( "/" + qtree ) 
   label += ( "_" + qtree ) 
  device = "%s:/%s" % ( svc_node, vol )
  
  print "%s:" % label
  print "  device: %s" % device
  print "  mount: %s" % mount
  print "  owner: %s" % owner
  print "  group: %s" % group
  print "  perms: %s" % perms

  if lenrow > 7 :
     print "  options: %s" % row[7]
