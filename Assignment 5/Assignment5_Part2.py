# Directions: Add try/except statements to catch the error. Identify the error and make a comment
# on the line above where you find it, but do not fix it.

# Geog 565 2016 Assignment 5 Part 2
# Name: Samantha Thompson       
# Date: 5.10.18
# This script unsucessfully attempts to buffer the parks.shp file.

import arcpy
from arcpy import env
env.overwriteOutput = True
# you may need to change this path to your own Exercise11 folder
env.workspace = "C:/EsriPress/Python/Data/Exercise11"
in_features = "parks.shp"
out_features = "parks_buf.shp"
##The buffer tool is invalid, it needs a buffer distance value.
try:
    arcpy.Buffer_analysis(in_features, out_features)
except arcpy.ExecuteError:
    print arcpy.GetMessages(2)
except:
    print "This does not have to do with the buffer tool."

        
