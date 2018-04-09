# Instructions:
# Create a script that determines if a list of integers contains duplicates.
# If it does contain duplicates, print out "This list contains duplicates".
# If the list does NOT contain duplicates, print out the smallest number in the list.
# Use the following lists for testing: [2, 8, 64, -16, 32, 4, 16, 8, -30] and [2, 8, 64, -16, 32, 4, 16, 18, -30]


# Name: Samantha Thompson   
# Date: 4.6.18
# Assignment 1 Part 4
# This script determines if a list of integers contains duplicates.

list1 = [2, 8, 64, -16, 32, 4, 16, 8, -30]
list2 = [2, 8, 64, -16, 32, 4, 16, 18, -30]

# your code here
list1.sort()
isDuplicate = False
for i in range(0, len(list1)-1):
    if list1[i] == list1[i+1]:
        isDuplicate = True
        break

if isDuplicate:
    print "This list contains duplicates."
else:
    print list1[0]

list2.sort()
isDuplicate = False
for i in range(0, len(list2)-1):
    if list2[i] == list2[i+1]:
        isDuplicate = True
        break

if isDuplicate:
    print "This list contains duplicates."
else:
    print list2[0]
