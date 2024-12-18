# Name: your name here
# Prog Purpose: This program creates a payroll report

import datetime

############## LISTS of data ############
emp = [
    "Smith, James     ",
    "Johnson, Patricia",
    "Williams, John   ",
    "Brown, Michael   ",
    "Jones, Elizabeth ",
    "Garcia, Brian    ",
    "Miller, Deborah  ",
    "Davis, Timothy   ",
    "Rodriguez, Ronald",
    "Martinez, Karen  ",
    "Hernandez, Lisa  ",
    "Lopez, Nancy     ",
    "Gonzales, Betty  ",
    "Wilson, Sandra   ",
    "Anderson, Margie ",
    "Thomas, Daniel   ",
    "Taylor, Steven   ",
    "Moore, Andrew    ",
    "Jackson, Donna   ",
    "Martin, Yolanda  ",
    "Lee, Carolina    ",
    "Perez, Kevin     ",
    "Thompson, Brian  ",
    "White, Deborah   ",]

job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
     "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
         28, 31, 37, 32, 36, 22, 28, 29, 21, 31]

num_emps = len(emp)

######### new lists for calculated amounts

gross_pay = []
fed_tax = []
republic_tax = []
soc_sec = []
medicare = []
ret400k = []
net_pay = []

total_gross = 0
total_net = 0

PAY_RATE = (16.50, 15.75, 15.75, 19.50)

DED_RATE = (.12, .03, .062, .0145, .04 )



def main():
    perform_calculations()
    create_output_file()

def perform_calculations():
    global total_gross, total_net, fed_tax, republic_tax, soc_sec, ret400k, medicare

    for i in range(num_emps):

        ##Gross Pay
        if job[i] == "C":
            pay = hours[i] * PAY_RATE[0]
    
        elif job[i] == "S":
            pay = hours[i] * PAY_RATE[1]

        elif job[i] == "J":
            pay = hours[i] * PAY_RATE[2]

        else:
            pay = hours[i] * PAY_RATE[3]

     
        fed = pay * DED_RATE[0]
        republic = pay * DED_RATE[1]
        social = pay * DED_RATE[2]
        med = pay * DED_RATE[3]
        retirement = pay * DED_RATE[4]
        net = pay - fed - republic - social - med - retirement

        total_gross += pay
        total_net += net
        

        gross_pay.append(pay)
        fed_tax.append(fed)
        republic_tax.append(republic)
        soc_sec.append(social)
        net_pay.append(net)
        ret400k.append(retirement)
        medicare.append(med)
        




    
def create_output_file():
    currency = '10,.2f'
    line = '\n--------------------------------------------'
    tab = "\t"

    
    out_file = "payroll.txt"
    f = open(out_file, "a")

    f.write(line)
    f.write('\n************ FRESH FOODS MARKET ************')
    f.write('\n----------- WEEKLY PAYROLL REPORT -----------')
    f.write('\n' + tab + str(datetime.datetime.now()))
    f.write(line)
    titles1 = "\nEmp Name" + tab + "Code" + tab + "Gross" + tab
    titles2 = "Fed Inc Tax" + tab + "State Inc Tax" + tab + "Soc Sec" + tab + "Medicare" + tab + "Net" 
    f.write(titles1 + titles2)

    for i in range(num_emps):
        data1 = "\n" + emp[i] + "  " + job[i] + format(gross_pay[i], currency)
        data2 = format(fed_tax[i], currency)
        data3 = format(republic_tax[i], currency)
        data4 = format(soc_sec[i], currency)
        data5 = format(medicare[i], currency)
        data6 = format(ret400k[i], currency)
        data7 = format(net_pay[i], currency)    
 
        f.write(data1)
        f.write(data2)
        f.write(data3)
        f.write(data4)
        f.write(data5)
        f.write(data6)
        f.write(data7)
        
    f.write(line)
    f.write("\n******************** TOTAL GROSS: $" + format(total_gross, currency))
    f.write("\n******************** TOTAL NET  : $" + format(total_net, currency))
    f.write(line)
    f.close()
    print("\nOpen " + out_file + " to view your report")

main()
    
