#! /usr/bin/env python

import os
import sys
import subprocess

# Steps:
#
# Change to root folder
#
# Swift:
# - make swift page
# 
# LAT LCs:
# - get list of objects
# - make folder for each object
# - for each object:
# - - change to folder
# - - download LAT LC for object 
# - - download swift LC for each object
# - - generate 4 plots
# - - extract last flux point for daily point 
# - - get LAT flux value and extrapolated VHE in terms of Crab (store)
# - - generate object visibility for coming night and coming month?
# - - generate web page for object
# - make main web page with LAT LCs and some text..


###########################################################################

# Change to root folder

root_folder = os.environ.get('BAR_ROOT')

quiet=False

if root_folder is None:
    if not quiet:
        print("No $BAR_ROOT set, exiting....")
    sys.exit(1)
    
try:
    os.chdir(root_folder)
except FileNotFoundError:
    if not quiet:
        print("{} does not exist, exiting...".format(root_folder))
    sys.exit(1)
except NotADirectoryError:
    if not quiet:
        print("{} is not a directory, exiting...".format(root_folder))
    sys.exit(1)

###########################################################################

###########################################################################

# make Swift web page

# default out file is: "Swift_LCs.html"
res=subprocess.call("makeSwiftLCHTML.py -c -l 7", shell=True)

###########################################################################

###########################################################################

# download LAT list

LC_File="LAT_LC_objects.txt"
DEC_min=32-50
DEC_max=32+50
RA_window=7
z_min=0
z_max=1.5
command="getFermiLCobjects.py -f {} -d {} {} -w {} -z {} {} -q".format(LC_File, DEC_min, DEC_max, RA_window, z_min, z_max)

print(command)
res=subprocess.call(command, shell=True)
print(res)

###########################################################################

# load txt file and extract names etc...

objects={}

with open(LC_File,"r") as f:
    for line in f:
        fields=line.split(",")
        object=fields[0].replace(" ","")
        objects[object]=(fields[1], fields[2], fields[3]) # RA, Dec, Redshift

print(objects)
        



  