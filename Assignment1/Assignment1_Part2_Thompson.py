# There are several ways to format strings. Please read section 4.12 of the
# textbook for more information. In this part of the assignment, please use
# the three different string formatting methods to print out the following
# string: 'A string is a sequence of characters'. Use the methods in whatever way you see fit.

# Name: Samantha Thompson
# Date: 4.6.18 
# Assignment 1 Part 2
# This script demonstrates the three different ways to format strings.


# method 1: the comma
str_list = ["A", "string", "is", "a", "sequence", "of", "characters."]
str_val = " ".join(str_list)
print str_val


# method 2: the + sign concatenator
print "A" + " string" + " is" + " a" + " sequence" + " of" + " characters."


# method 3: the format method
print "{0} {1} {2} {3} {4} {5} {6}".format("A", "string", "is", "a", "sequence", "of", "characters.")
