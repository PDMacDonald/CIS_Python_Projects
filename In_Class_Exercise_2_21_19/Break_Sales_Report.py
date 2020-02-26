#!/usr/bin/env python3
#shabang


"""
Break_Sales_Report.py: Break sales report for different reions of sorted data.
Data is expected to be in csv format.

CIS 3680-101
In-class exercise 2-21-19
"""

__author__ = "Preston MacDonald"
__copyright__ = "Copyright 2019, Preston MacDonald"
__credits__ = [""]
__license__ = ""
__version__ = "0.1.0"
__maintainer__ = "Preston MacDonad"
__email__ = "macdonaldpd@appstate.edu"
__status__ = "Complete"


#Retrieve and initialize variables
datafile = open("RegionSales.csv", "r")
region_total = 0
grand_total = 0
current_region = "1"

#Process header string
headerline = datafile.readline()
header = headerline.split(",")
print("\n", header[0], "    ", header[1], "      ",  header[2])
print("--------------------------------------")

#Process records
for dataline in datafile:

    #Split and read variables
    fields = dataline.split(",")
    store_number = fields[0]
    region = fields[1]
    sales = int(fields[2])
    
    #If we are processing a new region
    if(region != current_region):
        print("--------------------------------------")
        print("Region", current_region, "total  = ", region_total, "\n")
        grand_total += region_total
        current_region = region
        region_total = 0
        print("--------------------------------------")

    #Add to regional total and print
    region_total += sales
    print(" {store}         {reg}      {s:10}".format(store = store_number, reg = region, s= sales))


#Final output
grand_total += region_total
print("--------------------------------------")
print("Region:", current_region, "total  = ", region_total, "\n")
print("\ngrand_total = ", grand_total)