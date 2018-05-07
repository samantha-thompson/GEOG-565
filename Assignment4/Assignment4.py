# Name: Samantha Thompson
# Date: 5/6/2018
# Assignment 4


# Directions: You should already have gone through the instructions to make your data driven pages
# and you should have your Title and Overview pages ready as well.

# Write Python script to export selected map pages of your map to a PDF file and
# create a new PDF that includes the Title, Overview, and your exported pages.

# import arcpy and set up your workspace and environments


# create an arcpy.mapping.MapDocument using your mxd


# Export your Data Driven Pages to a PDF file
# provide the path and file name of the PDF so thath all pages will be exported
# If you want to just export certain pages, you must specify page number or page
# number range(s) if only selected pages will be exported


# create a fresh pdf document that will hold all of your pages
# use PDFDocumentCreate(pdf_path) function


# append the title page, the index pages, and the map pages to the PDF map book in that order
# assume the title page and index page are already created as PDF documents
# use PDFDocumentCreate function's appendPages method 3 times, one for title, one for overview, one for your exported pages


#use PDFDocumentCreate function's updateDocProperties method to update the mapbook title and authorship


#save and close the mapbook
#this is IMPORTANT - the changes made to the mapbook won't be saved if the script is closed before executing saveAndClose()


#delete reference to mapBookPDF


import arcpy
pdfpath = "C:/Users/saman/Desktop/GEOG 565/Assignment 4/Data/Mapbook.gdb/MapBook.pdf"
pdfdoc = arcpy.mapping.PDFDocumentCreate(pdfpath)

mapdoc = arcpy.mapping.MapDocument("C:/Users/saman/Desktop/GEOG 565/Assignment 4/Data/Assignment4_MapBook.mxd")
mapdoc.dataDrivenPages.exportToPDF("C:/Users/saman/Desktop/GEOG 565/Assignment 4/Data/Mapbook.gdb/Assignment4_MapBook.pdf")

pdfdoc.appendPages("C:/Users/saman/Desktop/GEOG 565/Assignment 4/Data/Mapbook.gdb/Reference Topographic Map Book of North Seattle.pdf")
pdfdoc.appendPages("C:/Users/saman/Desktop/GEOG 565/Assignment 4/Data/Mapbook.gdb/Overview.pdf")
pdfdoc.appendPages ("C:/Users/saman/Desktop/GEOG 565/Assignment 4/Data/Mapbook.gdb/Assignment4_MapBook.pdf")

pdfdoc.updateDocProperties(pdf_title="Reference Topographic Map Book of North Seattle",
                           pdf_author="Samantha Thompson")
                        
pdfdoc.saveAndClose()
del mapdoc
