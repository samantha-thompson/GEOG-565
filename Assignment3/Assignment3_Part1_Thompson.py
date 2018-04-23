# Geog 565 2016 Assignment 3 Part 1
# Name: Samantha Thompson
# Date: 4.22.18
# This script takes in a text file containing coordinates and turns it into a point shapefile.


# Directions: Create a Point shapefile that contains points whose coordinates are obtained 
# from the Assignment3_pointData.txt file, included in the Assignment3 starter package.
# Examine the content of this file before you begin. It contains an object ID and x y coordinates.
# Use the comments below to guide you, though feel free to ignore them and do it your own way. 

# File contents:
# OID: The object ID
# X: The x coordinate
# Y: The y coordinate
# Each point (coordinate pair x, y) in the text file becomes a point in the shapefile.


# import arcpy


# set up your workspace and environment


# create necessary variables


# create a variable to hold your new shapefile's name


# create a new featureclass in your workspace and make it type "Point"


# open textfile in readmode


# Create a list of all the lines in the file, but be sure to exclude the header!


# Create an Insert Cursor and give it your new feature class and the list of fields
# The geometry field you need is "SHAPE@XY"
# It is recomended that you create the cursor with a 'with' statement, though you don't have to


# Loop through the lines in your text file (except the header)
    
        # split the values using the split() function. (i.e. values = line.split(";")
        
        # assign variables to your x and y (use the index of the split values), you will need to cast your x and y as floats
        
        # create a rowValue variable to hold the list of attributes 

        # use cursor.insertRow(rowValue) to insert the row 

# delete the rowValue variable

# delete the cursor variable (unless you create the cursor with 'with' in which case it is automatically deleted)

# close the file


import arcpy
from arcpy import env

env.workspace = "C:/Users/saman/Desktop/GEOG 565/Assignment 3"
env.overwriteOutput = True

outpath = "C:/Users/saman/Desktop/GEOG 565/Assignment 3"
newfc = "/NewPoint.shp"

in_filepath = "Assignment3_pointdata.txt"
in_file = open(in_filepath, "r")

lines = []
for index, line in enumerate(in_file.readlines()):
        if index == 0:
                pass
        else:
                lines.append(line)

arcpy.CreateFeatureclass_management(outpath, newfc, "Point")
cursor = arcpy.da.InsertCursor(newfc, ["ID", "SHAPE@XY"])

for line in lines:
        values = line.split(";")
        oid = values[0]
        x = float(values[1])
        y = float(values[2])
        rowValue = [oid, (x, y)]
        cursor.insertRow(rowValue)
del rowValue
del cursor
in_file.close()
