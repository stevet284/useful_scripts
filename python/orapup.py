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
  if len(row) != 6:
    print "ERROR: line %s the csv needs 6 columns exactly" % line
    exit(1)
  
  svc_node=row[0]
  vol=row[1]
  qtree=row[2]
  mount=row[3]
  options=row[4]
  owner=row[5]
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

  if options:
    print "  options: %s" % options

  if ( mount in ora_mounts ) or ( mount in asm_mounts ):
    print "ERROR %s mount specifed more than once" % mount
    exit(2)
  
  if 'oracle' in owner:
   ora_mounts=ora_mounts + child_mounts(mount, ora_mounts)
  elif 'asm' in owner:
   asm_mounts=asm_mounts + child_mounts(mount, asm_mounts)
  else:
    print "ERROR: unrecognised owner: %s" % owner
    exit(1)

 print
 print
 print "asm_mounts %s " % asm_mounts
 print "ora_mounts %s " % ora_mounts
