#!/usr/bin/env python3
#shabang


"""
Main.py:  a program that allows a user to enter the size of the target 
population, the life expectancy of an individual in the population, and
the ages of the 12 infected individuals. Once this information is obtained, 
perform the above four calculations and output the result of each
calculation, appropriately labeled.

CIS 3680-101
In-class exercise 2-26-2019
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
INFECTED_COUNT = 12

run = "yes"

while(run.lower() == "yes"):
    infected_age_sum = 0

    #Input
    print("\nThis program estimates how many doses of an immunization drug you will need according to a set of inputs and calculations.")
    print("This program assumes your population is greater than 12 and have 12 sample ages of infected individuals in your population.\n")

    while(True):
        try:
            pop_size = int(input("Please input the size of your target population: "))
            break
        except ValueError:
            print("Incorrect input. Must be a integer!")
    while(True):
        try:
            life_expectancy = float(input("What is the life expectancy, in years, of a individual in your population:  "))
            break
        except ValueError:
            print("Incorrect input. Must be a real number!")


    for i in range(INFECTED_COUNT):
        while(True):
            try:
                print("Input age of infected person #", i+1, ":")
                age_of_infected = int(input())
                break
            except ValueError:
                print("Incorrect input. Must be a integer!")

        infected_age_sum += age_of_infected

    #Calculations
    average_infected_age = infected_age_sum / INFECTED_COUNT

    base_reproduction_number = life_expectancy / average_infected_age

    herd_immunity_threshold = 1 - (1 / base_reproduction_number)

    estimated_num_of_doses = math.ceil(herd_immunity_threshold * pop_size)
    

    #Output

    print("\nThe average infected age is: {0:.2f}".format(average_infected_age))
    print("The calculated base reproducion number is: {0:.2f}".format(base_reproduction_number))
    print("The calculated herd immunity threshold is: {0:.2f}".format(herd_immunity_threshold))
    print("The calculated required number of doses is: {0:.0f}".format(estimated_num_of_doses))
    print("\n")

    #Request to run again
    run = (input("enter \"yes\" to re-run the program: " ))
        




print("\n****** End of program *****\n")
#End of program