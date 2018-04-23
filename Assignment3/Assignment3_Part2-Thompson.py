# Geog 565 2016 Assignment 3 Part 2
# Name: Samantha Thompson   
# Date: 4.17.18


# Directions: Write a script that creates a new raster that meets certain
# slope, aspect, and land cover conditions. You will use the elevation and
# landcover.tif files from the Exercise 9 data folder. Here is the criteria:

# Moderate slope: between 10 and 20 degrees 
# Northeast aspect: between 0 and 90 degrees 
# Forested: land cover types of 41, 42, or 43

# Use the comments below for guidance.


# import arcpy


# import arcpy.sa

# set workspace

# check if the Spatial Analyst extention is available

    # check out the Spatial Analyst extention
    
# create a Raster object for your elevation

# create a Raster object for your landcover


# create slope and aspect variables to hold Slope and Aspect objects


# create a variable and assign it to your slope calculation

# create a variable and assign it to your aspect calculation

# create a variable and assign it to your landcover calculation

# calculate the final output

# save the output


# check in the Spatial Analyst Extention

import arcpy
from arcpy.sa import *

from arcpy import env

env.workspace = "C:/Users/saman/Desktop/GEOG 565/Assignment 3"
env.overwriteOutput = True

if arcpy.CheckExtension("Spatial") == "Available":
    arcpy.CheckOutExtension("Spatial")
else:
    print "The Spatial Analyst extension is not available"

# Moderate slope: between 10 and 20 degrees 
# Northeast aspect: between 0 and 90 degrees 
# Forested: land cover types of 41, 42, or 43
elevation_raster = arcpy.Raster("Exercise09/Elevation")
landcover_raster = arcpy.Raster("Exercise09/landcover.tif")

slope = Slope(elevation_raster, "DEGREE")
aspect = Aspect(elevation_raster)

moderateSlope = (slope <= 20) * (slope >= 10)
northeastAspect = (aspect >= 0) * (aspect <= 90)
forested = (landcover_raster == 41) | (landcover_raster == 42) | (landcover_raster == 43)

output_raster = (moderateSlope & northeastAspect & forested)

output_raster.save("output")

arcpy.CheckInExtension("Spatial")
