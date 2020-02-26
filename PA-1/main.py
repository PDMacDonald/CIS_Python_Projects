# Programming Assignment 1
# CIS3680-101 

# Author: Preston MacDonald
# Version: 01-29-2019

# Problem Prompt: 
# Design and construct a program to estimate the gallons of paint needed to 
# paint a wall and the estimated cost of the paint. Assume that one
# gallon of paint will cover 350 square feet of a wall, each doorway accounts
# for 14 square feet, and each window accounts for 8.5 square feet. Obtain all
# other required information from the user.
# The output of your program must include the total cost to purchase the paint
# and the number of gallons needed. Additional output may include the square
# footage of the wall and allowances made.

#Need this for ceiling function
import math

#Constants used in calculations

#Wall space covered in square feet by 1 gallon of paint.
paintCoverage = 350
#Wall space in square feet taken from 1 door
doorArea = 14
#Wall space in square feet taken from 1 window
windowArea = 8.5



#Introduction to program for user.
print("This program is designed to estimate the gallons of paint needed to paint a wall.")



# INPUTS

#Step 1: Need the user to input the dimensions of the room.
wallLength = float(input("Please input the length of the wall in feet:  "))
wallHeight = float(input("Please input the height of the wall in feet:  "))

#Step 2: Need the user to input the number of windows and doors in the room.
doors = int(input("Please provide the number of doors on the wall:  "))
windows = int(input("Please provide the number of windows on the wall:  "))

#Step 3: Need the user to input the cost of 1 gallon of their chosen paint.
galPaintCost = float(input("What is the cost in dollars, of 1 gallon of your desired paint:  "))



# CALCULATIONS 

#Step 4: Calculate wall space without doors or windows.
wallArea = wallLength * wallHeight

#Step 5: Calculate allowance for windows and doors.
doorAllowance = doors * doorArea
windowAllowance = windows * windowArea

#Step 6: Calculate the estimated wall space that needs to be painted.
paintArea = wallArea - doorAllowance - windowAllowance

#Step 7: Calculate how many gallons you need to cover the paint area.
paintGallons = math.ceil(paintArea / paintCoverage)

#Step 8: Calculate total cost to purchase the paint.
totalPaintCost = paintGallons * galPaintCost



#OUTPUT

#Step 8 Output the square footage of the wall and allowances made.
print("\nA wall with length", wallLength, "ft and height,", wallHeight, "ft is {0:.2f}".format(wallArea), "square feet.")
print("With", doors, "doors, the allowance for doors is {0:.2f}".format(doorAllowance), "square feet.")
print("With", windows, "windows, the allowance for windows is {0:.2f}".format(windowAllowance), "square feet.")
print("Making the total area for paint coverage {0:.2f}".format(paintArea), "square feet.")

#Step 9: Output the total cost to purchase the paint and the gallons needed.
print("\nYou need {0:.0f}".format(paintGallons), "gallons of paints to paint the wall.")
print("At {0:.2f}".format(galPaintCost), "for each gallon of paint, the total cost to purchase the paint is {0:.2f}".format(totalPaintCost), "dollars.")



# Added this line so when running program in non-terminal eniviroment, it will allow the user to see the results.
input("\nPress any key to end program......\n")
#End of Program


