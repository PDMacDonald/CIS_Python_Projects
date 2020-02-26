#!/usr/bin/env python3
#shabang


"""
LabLoop_pdm.py: A retirement planning calculator for Bee-Savin financial
services. The user should be able to enter the number of years they plan to 
continue working, how much they will invest each year, and the current rate of
return for their investment account. The output of the application is the 
amount they will have invested at the time they retire and a schedule that 
lists each year in retirement (year 0 is the year they retire) and the 
remaining balance. The schedule must account for yearly expenses and you may
assume the return rate after retirement is the same as prior to retiring.

CIS 3680-101
Programming Assignment #3
"""

__author__ = "Preston MacDonald"
__copyright__ = "Copyright 2019, Preston MacDonald"
__credits__ = [""]
__license__ = ""
__version__ = "0.1.0"
__maintainer__ = "Preston MacDonad"
__email__ = "macdonaldpd@appstate.edu"
__status__ = "Completed"


#Imports

#Input
print("\n")
print("This is an retirment planning calculator for Bee-Savin financial services.")
print("\n")

print("We will need a couple details to give you the amount that you will have invested at the time you retire.")
print("We will also use your information to produce a schedule that lists each year in retirement and the remaining balance")
print("\n")

yearly_retire_investment = float(input("How much will you invest towards retirement each year:  "))
years_of_work = int(input("How many years do you plan on working:  "))
current_rate = float(input("What is the current rate of return for your investment account (3% = 0.03):  "))
yearly_expenses = float(input("How much do you estimate your yearly expenses will be after retirement:  "))

#Process

#Calculate starting balance
balance = 0

for i in range(0, years_of_work):
    balance += yearly_retire_investment
    interest = balance * current_rate
    balance += interest


#Calculate ending balance
year = 0

print("\n")
print("Year   |   Balance")
print("-------------------------------------------------")
while(year < 40 and balance > 0):
    print("{0:4d}   |   {1:20.2f}".format(year, balance))
    balance -= yearly_expenses
    interest = balance * current_rate
    balance += interest
    year += 1
print("\n")
print("Note:  0 is the year you retire")


input("\nHit any key to end program...\n")

#End of program