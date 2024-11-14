# Name: Ciara Motter
# Prog Purpose: This program finds of a meal at Branch Barbeque Buffet
#   Price for an adult meal: $19.95
#   Price for a child meal: $11.95
#   service fee: 10%
#   Sales tax rate: 6.2%

import datetime

############# define global variables #############
# define tax rate, service fee, and prices
ADULT_MEAL = 19.95
CHILD_MEAL = 11.95
SALES_TAX_RATE = .062
SERVICE_FEE = .10

# define global variables
num_adult_meals = 0
num_child_meals = 0

############# define program functions #############
def main():

    more_meals = True

    while more_meals:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to order again (Y or N)? ")
        if yesno == "N" or yesno =="n":
            more_meals = False
            print("Thank you for your order. Enjoy your meal! ")


def get_user_data():
    global num_adult_meals
    num_adult_meals = int(input("number of adult meals:"))
    global num_child_meals
    num_child_meals = int(input("number of child meals if applicable:"))
    


def perform_calculations():
    global subtotal, sales_tax, service_fee, total
    subtotal = (CHILD_MEAL * num_child_meals) + (ADULT_MEAL * num_adult_meals)
    sales_tax = subtotal * SALES_TAX_RATE
    service_fee = subtotal * SERVICE_FEE
    total = subtotal + sales_tax + service_fee

def display_results():
    print('---------------------------------------')
    print('******* Branch Barbeque Buffet *******')
    print('Your local favourite Barbeque Buffet!!')
    print('---------------------------------------')
    print('Meal costs             $ ' + format(subtotal,'8,.2f'))
    print('Sales Tax              $ ' + format(sales_tax,'8,.2f'))
    print('Service fees           $ ' + format(service_fee,'8,.2f'))
    print('Total                  $ ' + format(total,'8,.2f'))
    print('---------------------------------------')
    print(str(datetime.datetime.now()))

############# call on main program to execute #############
main()
