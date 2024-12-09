# Ciara Motter
#Prog purp: Read in a list of customers and display a report that will increase the amount they owe about 10% if payment is late
# Data file is .csv

infile = "customer_data_file.csv"

cust_in_data_block_list = []
cust = []

LATE_FEE_RATE = .10
grand_total = 0

def main():
    read_in_cust_file()
    perform_calculations()
    display_cust_report()

def read_in_cust_file():
    global cust  # Ensure we can modify the global `cust` list
    cust_data_file = open(infile, "r")

    cust_in_data_block_list = cust_data_file.readlines()
    cust_data_file.close()

    for line in cust_in_data_block_list:
        # Remove whitespace and split on commas
        line = line.strip().split(", ")

        cust.append([line[0], line[1], float(line[2]), int(line[3])])


def perform_calculations():
    global grand_total

    for i in range(len(cust)):
        amt_owed = float(cust[i][2])
        days_late = int(cust[i][3])

        if days_late > 0:
            late_fee = amt_owed * LATE_FEE_RATE

        else:
            late_fee = 0

            amt_owed += late_fee
            grand_total += amt_owed
            cust[i][2] = amt_owed

def display_cust_report():
    
    currency = "8,.2f"
    line = "--------------------------------------"
    tab = "\t"

    print(line)
    print("***** CUSTOMER BALANCE REPORT *******")
    print(line)

    for i in range(len(cust)):
        print(f"{cust[i][1]} {cust[i][0]}{tab}${format(cust[i][2], currency)}")

    print(line)
    print(f"**** GRAND TOTAL: \${format(grand_total, currency)}")


main()
