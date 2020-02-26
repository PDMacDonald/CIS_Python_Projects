

#!/usr/bin/env python3

"""
cash_register.py: #Cash register program that allows a user to enter a list of
 item prices. Then prints a basic receipt that includes a header and footer. 
 The prices Entered, the order subtotal, amount of tax on the order, and the overall
 Total to be paid. Functions are used in program design. The individual prices
 Are stored in a list container for processing and all decimal points are 
 aligned in output.

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


from datetime import datetime


#Function used to run the cash_register application.
def run_cash_register(tax_rate):

    register_intro()

    price_list = get_price_list()

    calculations = receipt_calculations(price_list, tax_rate)

    print_receipt(tax_rate, price_list, calculations)
    


 
#Function that handles the introduces to the cash register to the user.
def register_intro():
    print("\n\nWelcome to Mac's innovated cash register system that tackles your pricing needs!") 
    print("After entering all the prices in the register, the system will provide you with a subtotal,") 
    print("amount of tax on the order, and the overall total to be paid in the form of a basic receipt.")
    
    print()
    print("***Instructions***")
    print("Please enter a valid price for each item. If you make a mistake the system will indicate that")
    print("a error occured and reprompt you to give a proper price. The system will round to 2 decimal places.")
    print("To end price input, press Enter.")

    print("\n\n")


#Function that gets a list of floats that are rounded to the 2nd decimal place to reflect a price list.
#User will hit enter to end the list.
def get_price_list():
    float_list = []
    i = 0
    while(True):

        i += 1
        float_input = input("Item #{0} price: ".format(i))

        if(float_input == ""):
            break
        else:
            try:
                float_input = round(float(float_input), 2)
                float_list.append(float_input)
            except ValueError:
                i -= 1
                print("Invalid Price!")

    return float_list


#Function that performs all needed calculations for the receipt.
def receipt_calculations(prices, tax_rate):
    item_count = len(prices)
    subtotal = sum(prices)
    tax_amount = tax_rate * subtotal
    total = subtotal + tax_amount

    return (item_count, subtotal, tax_amount, total)


#Prints a receipt with formatted price list and calculations.
def print_receipt(tax_rate, prices, calculations):

    print("\n")
    print("                         Your Receipt")
    print("-------------------------------------------------------------------")
    print("Current date and time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("\n")

    for i in range(0, len(prices)):
        print("Item #{0:4}   -----> {1:12.2f}".format(i+1, prices[i]))
    
    print()
    print("Total Items: {0}".format(calculations[0]))
    print()
    print("Sub-Total: {0:.2f}".format(calculations[1]))
    print("Tax Rate: {0:.4f}".format(tax_rate))
    print("Tax Amount: {0:.2f}".format(calculations[2]))
    print("Total: {0:.2f}".format(calculations[3]))
    print("\n")



