# Be sure you have gone through Exercises 2 and 5 including the challenge exercises
# from the textbook before attempting this part.

# This exercise is to get you familiarized with ModelBuilder and ArcGIS and how
# we can use Python to modify and enhance our workflows. You will find the data you need for this
# part in the Data folder that came with the assignment.
# Using this data, use Model Builder to build a model that does the following:

# 1. Defines the projection for each dataset to WA State Plane North FIPS 4601.
# 2. Clips the roads and trees datasets based on the UDistrict boundary
# Then, convert your model to a Python script called UDistrict.py.
# Inspect the code that is automatically generated and try to understand what it produces.

# Modify the generated script and do the following:
# Create a list of files (feature classes) needed (e.g., myList = ["fc1", "fc2", "fc3"])
# Use a loop to define projection of each file (for loop)
# Use a loop to clip the streets and trees using the UDistrict boundary (for or while loop)

# Name: Samantha Thompson
# Date: 4.8.18
# Assignment 1 Part 5
# This script is a modified output of Model Builder that projects and clips data in the University District

# your code here
# Import arcpy module
import arcpy


# Local variables:
seattleRoads = "seattleRoads"
seattleRoads_Projection = seattleRoads
uDistrict = "uDistrict"
uDistrict_Projection = uDistrict
seattle_Roads_Clip_shp = "C:\\Users\\saman\\Desktop\\GEOG 565\\Data\\seattle_Roads_Clip.shp"
seattleTrees = "seattleTrees"
seattleTrees_Projection = seattleTrees
seattle_Trees_Clip_shp = "C:\\Users\\saman\\Desktop\\GEOG 565\\Data\\seattle_Trees_Clip.shp"




fcList = [seattleRoads, uDistrict, seattleTrees]
for fc in fcList:
    arcpy.DefineProjection_management(fc, "PROJCS['NAD_1983_HARN_StatePlane_Washington_North_FIPS_4601_Feet',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.8333333333333],PARAMETER['Standard_Parallel_1',47.5],PARAMETER['Standard_Parallel_2',48.73333333333333],PARAMETER['Latitude_Of_Origin',47.0],UNIT['Foot_US',0.3048006096012192]]")

clipList = [
    (seattleRoads_Projection, seattle_Roads_Clip_shp),
    (seattleTrees_Projection, seattle_Trees_Clip_shp)
]
for clip in clipList:
    arcpy.Clip_analysis(clip[0], uDistrict_Projection, clip[1], "")
