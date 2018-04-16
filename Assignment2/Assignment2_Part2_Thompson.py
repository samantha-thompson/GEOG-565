# Directions: Using the lakes.shp file from the Exercise 2 folder, create a script that
# adds a new field called AreaClass (type Text), and then uses the AREA_ column to classify
# each lake as "Small", "Medium", or "Large" in this field.
# Hint: we already did this in the Field Calculator, but now we're doing it in a stand-alone script!

# Small - Area less than 35000
# Medium - Area greater than or equal to 35000 and less than 120000 feet
# Large - Area greater than or equal to 120000 feet

# Geog 565 2016 Assignment 2 Part 2
# Name: Samantha Thompson
# Date: 4.14.18

# This script adds a new field to a shapefile, then populates it with the size classification.
# import modules
# set workspace
# define a variable for our shapefile
# add a new field to hold our area class
# We need to make changes to the attribute table, and to do that we need to create an update cursor
# Use the AREA_ field and the new SizeClass field in the cursor
# populate SizeClass based on the value in AREA_ specified in the Directions
    # loop though the cursor
        # if area is small, define SizeClass as Small
        # if area is medium, define SizeClass as Medium
        # if area is large, define SizeClass as Large
        # update the row with the appropriate value - Don't forget this step!
# delete your row variable
# delete your cursor variable

import arcpy
from arcpy import env
env.workspace = "C:/Users/saman/Desktop/GEOG 565/Assignment 2"

fc = "lakes.shp"
newfield = "AREACLASS"
fieldtype = "TEXT"
fieldname = arcpy.ValidateFieldName(newfield)
arcpy.AddField_management (fc, fieldname, fieldtype, "", "", 10)
print "New field AreaClass created."


cursor = arcpy.da.UpdateCursor(fc, ["AREA_", "AREACLASS"])
for row in cursor:
    if (row[0] < 35000):
        row[1] = "Small"
    elif (row[0] >= 35000 and row[0] < 120000):
        row[1] = "Medium"
    elif (row[0] >= 120000):
        row[1] = "Large"
    cursor.updateRow(row)
del row
del cursor
print "Rows in AreaClass updated with size classification."

