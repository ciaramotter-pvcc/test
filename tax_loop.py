# Ciara Motter
# Prog Purpose: This Program calculates the Personal Property Tax bill

import datetime
# Define assesed value and tax
TAX_RATE = .440
TAX_RELIEF = .30
SIX_MONTH_RELIEF = .33

# Global Variables
inout = 1 #1 means yes, one means no
tax_amount = 0
six_month_bill = 0
assessed_value = 0
relief_amount = 0
six_month_relief = 0
full_annual = 0
total = 0

######## Define program functions
def main():

    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to calculate another vehicles' personal property tax bill?")
        if yesno == "n" or yesno == "N":
            more = False
            print("Thank you for calculating your bill.")

def get_user_data():
    global inout, assessed_value
    print('**** PERSONAL PROPERTY TAX BILL ****')
    inout = int(input("Enter 1 if your vehicle is eligible for relief; enter a 2 if you are not eligible for tax relief: "))
    assessed_value = int(input("Enter your assesed value of your vehicle: $ "))

def perform_calculations():
    global tax_amount, six_month_bill, assessed_value, relief_amount, full_annual, six_month_relief, total
    
    if inout == 1:
        tax_amount = assessed_value * TAX_RATE
        six_month_bill = tax_amount / 2
        relief_amount = six_month_bill * TAX_RELIEF
        six_month_relief = six_month_bill * SIX_MONTH_RELIEF
        total = six_month_bill - relief_amount
    else:
        tax_amount = assessed_value * TAX_RATE
        six_month_bill = tax_amount / 2
        relief_amount = six_month_bill * 0
        six_month_relief = 0
        total = six_month_bill

def display_results():
    currency = '8,.2f'
    line = '---------------------------------------------------'

    print(line)
    print('**** PERSONAL PROPERTY TAX BILL ****')
    print('     please pay in a timely manner.')
    print(str(datetime.datetime.now()))
    print(line)
    print('Assessed Value            $ ' + format(assessed_value, currency))
    print('Relief Amount             $ ' + format(relief_amount, currency))
    print('Six Month Relief amount   $ ' + format(six_month_relief, currency))
    print('Full Annual Amount        $ ' + format(tax_amount, currency))
    print(line)
    print('Total                     $ ' + format(total, currency))

main()

          
         

