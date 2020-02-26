#!/usr/bin/env python3
#shabang


"""
Midterm.py: A program that allows an operator to enter the lengths of 10 bolts
randomly selected for testing. Once the 10 lengths have been entered output 
the mean of the sample, a message indicating if the batch passes/fails based on
the mean, the number of bolts outside the tolerance range, and a message
indicating if the batch passes/fails based on number of bolts outside tolerance.


CIS 3680-101
Mid term - 2-28-2019
"""

__author__ = "Preston MacDonald"
__copyright__ = "Copyright 2019, Preston MacDonald"
__credits__ = [""]
__license__ = ""
__version__ = "0.1.0"
__maintainer__ = "Preston MacDonad"
__email__ = "macdonaldpd@appstate.edu"
__status__ = "Complete"

import math

#Constants
TOL = 0.125
EXPECTED_MEAN = 4.0
MAX_BOLT_OUT_OF_RANGE = 2

#Retrieve and initialize variables
datafile = open("data.csv", "r")
bolts_out_of_range = 0
number_of_bolts = 0
sum_of_lengths = 0

#Obtain file inputs and process
print("\nThis program will calculate the mean and standard deviation of a given data file that contains only a single column of bolt lengths.")
print("The program will then procede to check if the average bolt length is within tolerance of the expected mean of", EXPECTED_MEAN, "with tolerance of", TOL)
print("Furthermore, it will check to see if the number of bolts that are outside the tolerance does not exceed", MAX_BOLT_OUT_OF_RANGE)


for dataline in datafile:
    bolt = float(dataline)
    number_of_bolts += 1
    sum_of_lengths += bolt

    if(bolt < (EXPECTED_MEAN - TOL)) or (bolt > (EXPECTED_MEAN + TOL)):
        bolts_out_of_range += 1
datafile.close()


#Calculation of Average
avg_bolt_length = sum_of_lengths / number_of_bolts

#Calculation of Standard Deviation
sum_of_squared_dif = 0

#Could use a list to make this more efficient but, I didn't want to use 
# something that wasn't covered in class yet
datafile = open("data.csv", "r")
for dataline in datafile:
    bolt = float(dataline)
    sum_of_squared_dif += (bolt - avg_bolt_length)**2
datafile.close()

standard_dev_of_bolts = math.sqrt(sum_of_squared_dif / number_of_bolts)


#Output
print("\nCalculated mean of sample: {0:.4f}".format(avg_bolt_length))
print("Calculated standard deviation of sample: {0:.4f}".format(standard_dev_of_bolts))
print("Number of bolts outside tolerance range:", bolts_out_of_range)

if(avg_bolt_length < (EXPECTED_MEAN - TOL)) and (avg_bolt_length > (EXPECTED_MEAN + TOL)):
    print("Batch passes/fails based on calculated sample mean: FAIL")
else:
    print("Batch passes/fails based on calculated sample mean: PASS")

if(bolts_out_of_range > MAX_BOLT_OUT_OF_RANGE):
    print("Batch passes/fails based on number of bolts outside tolerance: FAIL")
else:
    print("Batch passes/fails based on number of bolts outside tolerance: PASS")


input("\n***** Hit enter key to end the program *****\n")
#End of program
