#!/usr/bin/env python3
#shabang


"""
Personal_Signs.py: Application to compute the price of any sign a customer
orders, based on the following facts:

1. The minimum charge for all signs is $30.
2. If the sign is made of oak, $15. No charge is added for pine.
3. The first six letters or numbers are included in the minimum charge; there
   is an additional $3 charge for each additional character.
4. Black or white characters are included in the minimum charge; there is an
   additional $12 charge for gold-leaf lettering.

CIS 3680-101
Programming Assignment #2
Last Modified: 2-11-2019
"""

__author__ = "Preston MacDonald"
__copyright__ = "Copyright 2019, Preston MacDonald"
__credits__ = [""]
__license__ = ""
__version__ = "0.1.0"
__maintainer__ = "Preston MacDonad"
__email__ = "macdonaldpd@appstate.edu"
__status__ = "Completed"

#imports

#Define Constants
MIN_CHRG_USD = 30 #Minimum charge for all signs in US Dollars (USD)
OAK_CHRG_USD = 15 #Charge for signs of oak type make in USD.
NO_CHRG_CNT = 6 #The number of letters included in minimum charge.
ADD_CHAR_CHRG_USD = 3 #Charge for additional characters in USD.
GOLD_LEAF_CHRG_USD = 12 #Charge for gold leaf lettering in USD.


#Input
print("\n")
print("Welcome to the personalized signs price calculator!")
print("NOTE: if invalid input is given for sign options, the default option will be selected.")
print("\n")
print("All signs have a minimum charge of", MIN_CHRG_USD, "US Dollars (USD).")
print("\n")

print("The first", NO_CHRG_CNT, "characters are free.")
print(ADD_CHAR_CHRG_USD, "USD will be charged for each additional character.")
print("NOTE: Spaces are not considered in the character count or for additional charges.")
sign_str = input("What would you like to print on your personalized sign?  ")
print("\n")

print("We offer 2 different materials to make your sign.")
print("The default option is pine which is included in the minimum charge (DEFAULT).")
print("The upgraded option is oak which costs an additional", OAK_CHRG_USD, "USD.")
is_oak = input("Would you like to upgrade your sign to oak ? (Y / N): ")
print("\n")

print("We offer 3 types of lettering for your sign.")
print("B = Black lettering (Included in minimum charge) (DEFAULT).")
print("W = White lettering (Included in minimum charge).")
print("G = Gold leaf lettering (", GOLD_LEAF_CHRG_USD, "USD upcharge).")
lettering_type = input("What lettering type would you like for your sign? (W / B / G):  ")


#Process / Computations
additional_charges = 0

#Charge for additional characters
char_cnt = len(sign_str) - sign_str.count(" ")

if(char_cnt > NO_CHRG_CNT):
    additional_charges += (3 * (char_cnt - NO_CHRG_CNT))

#Charge for sign material
if(is_oak.upper() == 'Y'):
    additional_charges += OAK_CHRG_USD

#Charge for lettering
if(lettering_type.upper() == 'G'):
    additional_charges += GOLD_LEAF_CHRG_USD


#Output

#List sign properties according to input
print("\n")
print("Sign Properties: ")
print("Your sign will Read: ", sign_str)
print("Character count (not including spaces): ", char_cnt)
#Sign material
if(is_oak.upper() == 'Y'):
    print("Sign material: Oak")
else:
    print("Sign material: Pine")
#Sign lettering
if(lettering_type.upper() == 'G'):
    print("Sign lettering: Gold leaf")
elif(lettering_type.upper() == 'W'):
    print("Sign lettering: White")
else:
    print("Sign lettering: Black")
print("\n")

print("The minimum charge for a personalized sign is", MIN_CHRG_USD, "USD.")
print("Based on your options, you have an additional charge of", additional_charges, "USD.")
print("The total cost of your personalized sign is", MIN_CHRG_USD + additional_charges, "USD.")



input("\nPress any key to end the program...\n")

#End of program

