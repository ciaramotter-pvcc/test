# Name: your-name-here
# Prog Purpose: This program finds the cost of movie tickets, popcorn, & drinks
#   The output is sent to an .html file

import datetime

##############  define global variables ############
# define tax rate and prices
RATE_TUITION_IN = 164.40
RATE_TUITION_OUT = 353.00
RATE_CAPITAL_FEE = 26.00
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

# define global variables
inout = 1 # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarship_amt = 0

tuition_amt = 0
inst_fee = 0
cap_fee = 0
act_fee = 0
total = 0
balance = 0

# create output file
outfile = 'tickets.html'


##############  define program functions ################
def main():
    
    open_outfile()
    more_tickets = True
    
    while more_tickets:
        get_user_data()
        perform_calculations()
        create_output_file()
        
        askAgain = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if askAgain.upper() == 'N':
            more_tickets = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Cinema House Movies </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #505A5B; background-image: url(wp-pvcc.png); color: #141414;">\n')
    
def get_user_data():
    global inout, numcredits, scholarship_amt
    print('**** PIEDMONT VIRGINIA COMM COLLEGE Tuition & Fees ****')
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarship_amt = int(input("Scholarship amount recieved: "))   

def perform_calculations():
    global tuition, inst_fee, cap_fee, act_fee, total, balance

    if inout == 1:
        tuition = numcredits * RATE_TUITION_IN
        cap_fee = 0
        act_fee = numcredits * RATE_ACTIVITY_FEE
        inst_fee = numcredits * RATE_INSTITUTION_FEE
        total = tuition + act_fee + act_fee + inst_fee
        balance = total - scholarship_amt
    else:
        tuition = numcredits * RATE_TUITION_OUT
        cap_fee = numcredits * RATE_CAPITAL_FEE
        act_fee = numcredits * RATE_ACTIVITY_FEE
        inst_fee = numcredits * RATE_INSTITUTION_FEE
        total = tuition + act_fee + act_fee + inst_fee + cap_fee
        balance = total - scholarship_amt

def create_output_file():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "3">'
    sp = " "

    f.write('\n<table border="3"   style ="background-color: #94B0DA;  font-family: arial; margin: auto;">\n')            
    f.write(colsp + '\n')
    f.write('<h2>**** PEIDMONT VIRGINIA COMM COLLEGE ****</h2></td></tr>')
    f.write(colsp + '\n')
    f.write('*** Tuition and Fees Report ***\n')
    
    f.write(tr + 'Tuition' + endtd + str(tuition) + endtd + format(tuition,currency) + endtr)
    f.write(tr + 'Capital Fee' + endtd + str(cap_fee) + endtd + format(cap_fee,currency) + endtr)
    f.write(tr + 'Instuition Fee ' + endtd + str(inst_fee) + endtd +  format(inst_fee,currency)  + endtr)
    f.write(tr + 'Activity Fee ' + endtd + str(act_fee) + endtd + format(act_fee, currency) + endtr)

    f.write(tr + 'Total' +  endtd + sp + endtd + format(total,currency)  + endtr)     
    f.write(tr + 'Remaining Scholarship balance' + endtd + sp + endtd + format(balance,currency) + endtr)
    
    f.write(colsp + 'Date/Time: '+ day_time + endtr)
    f.write('</table><br />')


##########  call on main program to execute ############
main()              


