# Directions: Complete the functions below. The first one is done for you. The tests at the bottom should run
# and print out values you'd expect. 

# Geog 565 2016 Assignment 6 Part 1
# Name: Samantha Thompson
# Date: 5.13.18
# This script creates and test 3 functions

# the triangle fucntion takes in 3 numbers and returns the type of triangle

def triangle(a, b, c):
    if a == b == c:
        return "equilateral"
    elif (a != b and a != c and b != c):
        return "none"
    else:
        return "isosceles"

# the absolutevalue function takes in an integer and returns the absolute value of that integer
# you can assume there will only be integers as input
# the absolute value of a number is always positive
# for example: the absolute value of 5 is 5; the absolute value of -5 is 5

def absolutevalue(x):
    if x < 0:
        return x * -1
    else:
        return x




# the absolutevalues function takes in a list of integers and returns a list of the absolute values of the original list
# this is similar to the absolutevalue function except you need to loop through the input list and return a list

def absolutevalues(intList):
    absList = []
    for x in intList:
        absList.append(absolutevalue(x))
    return absList
    



# Tests - do not remove. These will help you know your functions are working. Feel free to add more!

# triangle tests

print triangle(2,2,2)
print triangle(2,2,5)
print triangle(1,2,3)

# absolutevalue tests

print absolutevalue(-5)
print absolutevalue(10)

# absolutevalues tests

print absolutevalues([1,2,-2,-5])
print absolutevalues([-11,-12,2,-5]) 
