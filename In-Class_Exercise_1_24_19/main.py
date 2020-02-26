# In-Class Exercise 01-24-2019
# CIS3680-101 

# Author: Preston MacDonald
# Version: 01-24-2019

# Problem Prompt: 
# Design and build a program to calculate a persons Body Mass Index (BMI). 
# The program must accept the individuals height in inches and their weight
# in pounds. It should then convert the measures to metric units, perform 
# the calculation, and output the result.

# BMI = weight (kilograms) / height^2 (meters)



#Step 1: Take input for height in inches and weight in lbs.
#Step 2: Convert inches to meters and lbs to kilograms.
#Step 3: Use converted values to calculate BMI
#Step 4: Print BMI




#Step 1 take in input
print("This program will calculate your Body Mass Index (BMI).")

heightInches = int(input("Please type in your height in inches:  "))
weightLbs = int(input("Please type in your weight in pounds:  "))



#Step 2 Convert inches to meters and lbs to kilogram for BMI calculation

# 1 inch = 0.0254
InToM = 0.0254
# 1 lb = 0.4536
LbsToKg = 0.453592

heightMeters = heightInches * InToM
weightKilograms = weightLbs * LbsToKg


#Step 3 Calculate BMI
bmi = weightKilograms / (heightMeters ** 2)


#Step 4 Output BMI
print("Your BMI is: {0:5.1f}".format(bmi))