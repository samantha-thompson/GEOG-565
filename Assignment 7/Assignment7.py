# Geog 565 2016 Assignment 7
# Name: Samantha Thompson       
# Date: 5.27.18

# Directions: Use this script to build a script tool in ArcMap.
# Examine this script and make sure you understand what it does. Modify the input, output,
# and interval variables to be user-defined using GetParameterAsText. These are the only
# changes you should need to make.
# Test the script in PythonWin before creating your script tool.
# Use Exercise 13 as a guide when making your tool.

# import arcpy
import arcpy
from arcpy.sa import *
from arcpy import env

# set up the user-defined variables using GetParameterAsText

# input will be the first parameter. It should have GetParameterAsText at index 0
input = arcpy.GetParameterAsText(0)
# output will be the second parameter. It should have GetParameterAsText at index 1
output = arcpy.GetParameterAsText(1)
# interval will be the third parameter. It should have GetParameterAsText at index 2
# since this parameter is an integer and not text, you need to cast the value as an integer
interval = int(arcpy.GetParameterAsText(2))

# this script creates a contour shapefile 
try:
    # check if the Spatial Analyst extention is available
    if arcpy.CheckExtension("Spatial") == "Available":
        # if available, check it out
        arcpy.CheckOutExtension("Spatial")
        print "Checked out Spatial Analyst extension"
    else:
        # otherwise, print a message
        print "Spatial Analyst license is unabailable"
    # do the contouring using user defined variables
    Contour (input, output, interval)
    print "Contour complete"

except arcpy.ExecuteError:
    print arcpy.GetMessages(2)

except:
    print "There has been a non-tool error"

finally:
    # check in the Spatial Analyst extention
    arcpy.CheckInExtension('Spatial')
    print "Spatial Analyst extention checked in"
