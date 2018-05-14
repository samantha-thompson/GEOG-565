# Directions: Fix the syntax errors in this script. When you find them, make a comment above the
# line describing the problem and how you fixed it.

# Geog 565 2016 Assignment 5 Part 1
# Name: Samantha Thompson
# Date: 5.10.18
# This script prints the name of each park in the parks.shp file

import arcpy
from arcpy import env
# you may need to change this path to point to your own Exercise11 folder
env.workspace = "C:/EsriPress/Python/Data/Exercise11"
##changed "FC" to "fc" 
fc = "parks.shp"
rows = arcpy.SearchCursor(fc)
fields = arcpy.ListFields(fc)
##added a colon for the for loop
for field in fields:
    if field.name == "PARK_NAME":
        for row in rows:
          print "Park Name = {0}".format(row.getValue(field.name))
          
