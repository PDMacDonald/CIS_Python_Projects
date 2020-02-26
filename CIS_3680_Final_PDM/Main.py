#!/usr/bin/env python3

"""
Main.py: Main code file to run code responsible for creating a report that
    quantitatively describes each variable in a dataset for Crystal Ball 
    Analytics.

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

import CSV_Utilities as CSV

csv_filename = "Exam-Data-Dstat.csv"
has_headers = True

data_table = CSV.read_csv(csv_filename, has_headers)

print(data_table.items())
