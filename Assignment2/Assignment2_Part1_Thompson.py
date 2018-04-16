# Directions: Using all the data in the Exercise06 folder, create a script that copies all of the
# point and line (not polygon) feature classes into a new database that the script creates.

# Geog 565 2016 Assignment 2 Part 1
# Name: Samantha Thompson
# Date: 4.14.18

# This script looks at all of the feature classes in a workspace and copies all of the point and line feature classes
# into a new database that the script creates.


# import modules


# set workspace


# allow overwriting


# create new geodatabase


# print out that the geodatabase was successfully created (this is very nice for the user, but not necessary for the script's purpose


# set a variable equal to a list of the feature classes in the workspace (use an arcpy function to do this)


# loop through each feature class in the list of feature classes
# use arcpy.Describe to set variables to the feature class name and shapeType
# if the shapeType is Point or Polyline, add it to the new geodatabase
# otherwise, if the shapeType is Polygon, do nothing
# add print statements as needed so the user knows what's going on when they run the script!

import arcpy
from arcpy import env

env.overwriteOutput = True
env.workspace = "C:/EsriPress/Python/Data/Exercise06"
arcpy.CreateFileGDB_management("C:/EsriPress/Python/Data/Exercise06/Results", "Assignment_2.gdb")
print "GDB Created"

fclist = arcpy.ListFeatureClasses()
print fclist

for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    shapeType = fcdesc.shapeType
    
    if shapeType in ['Point', 'Polyline']:
        arcpy.CopyFeatures_management(fc, "C:/EsriPress/Python/Data/Exercise06/Results/Assignment_2.gdb/" + fcdesc.basename)
        print "Adding", shapeType, "to GDB as", fc
    else:
        print "Skipping", shapeType, "to GDB as", fc

