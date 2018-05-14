# Directions: Complete the function below. 

# Geog 565 2016 Assignment 6 Part 2
# Name: Samantha Thompson
# Date: 5.13.18
# This script creates and tests the listpolygons function

# the listpolygons function takes in a workspace path and returns a list of
# all the polygons in that workspace
# for example, using your exercise 2 folder as the input workspace should print this to the console:
# [u'parks.shp', u'zip.shp']

import arcpy
def listpolygons(workspace):
    arcpy.env.workspace = workspace
    return arcpy.ListFeatureClasses(feature_type = "polygon")
   


# Tests - Feel free to add more workspaces to test your function. Modify the workspace paths if necessary to
# point to your own exercise folders.

# this test should print out a list of all the polygons in your exercise 2 folder
print listpolygons(r'C:\EsriPress\Python\Data\Exercise02')

# this test should print out a list of all the polygons in your exercise 5 folder
print listpolygons(r'C:\EsriPress\Python\Data\Exercise05')
