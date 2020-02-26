
#!/usr/bin/env python3

"""
main.py: Runs cash_register.py (Cash Register Program)

CIS3680-101 
Programming Assignment
"""

__author__ = "Preston MacDonald"
__copyright__ = "Copyright 2019, Preston MacDonald"
__credits__ = [""]
__license__ = ""
__version__ = "0.1.0"
__maintainer__ = "Preston MacDonald"
__email__ = "macdonaldpd@appstate.edu"
__status__ = "Complete"

#Load libraries
import cash_register

#Constants
TAX_RATE = .0725

# Run cash register program.
cash_register.run_cash_register(TAX_RATE)





