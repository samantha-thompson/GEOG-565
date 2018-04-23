# Geog 565 2016 Assignment 3 Part 3
# Name: Samantha Thompson
# Date: 4.17.18

# Directions: Using the q1222.dem file in the NSeattleDEM folder included in the starter zip,
# create a contour file that uses an interval that the user specifies. You must use arcpy.GetParameterAsText for this.
# Be sure to test your script using different intervals.


# import arcpy

# import arcpy.sa

# set your environment variables


# get your interval from the user using arcpy.GetParameterAsText


# check out the Spatial Analyst extention if its available


# do the contouring


# check in the Spatial Analyst extention

import arcpy
from arcpy.sa import *

from arcpy import env

env.workspace = "C:/Users/saman/Desktop/GEOG 565/Assignment 3"
env.overwriteOutput = True

contourInterval = int(arcpy.GetParameterAsText(0))

if arcpy.CheckExtension("Spatial") == "Available":
    arcpy.CheckOutExtension("Spatial")
else:
    print "The Spatial Analyst extension is not available"

inRaster = "NSeattleDEM/q1222.dem"
outContours = "outcontours"
baseInterval = 0
Contour(inRaster, outContours, contourInterval, baseInterval)

arcpy.CheckInExtension("Spatial")
