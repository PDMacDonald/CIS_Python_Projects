#!/usr/bin/env python3

"""
Read_CSV_Utilities.py: Code responsible for reading a CSV file into a dictionary
    for processing in python.

CIS3680-101 
Final Exam Program
Date created: 05/03/2019
"""

__author__ = "Preston MacDonald"
__copyright__ = "Copyright 2019, Preston MacDonald"
__credits__ = [""]
__license__ = ""
__version__ = "0.1.0"
__maintainer__ = "Preston MacDonald"
__email__ = "macdonaldpd@appstate.edu"
__status__ = "Complete"



def read_csv(csv_file, has_headers):

    file = open(csv_file, "r")
    headers = []
    data_table = dict()

    #read in headers
    if(has_headers):
        data_string = file.readline()

        headers = data_string.strip(",")

        for header in headers:
            data_table.update({header : [] })



    #Read in records
    for record in file:
        
        data = record.strip(",")

        for i in range(len(header)):
            
            data_table.get(header[i]).append(data[i])

    return data_table
        






        
