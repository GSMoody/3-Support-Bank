import csv
import sys
import logging
logging.basicConfig(filename='SupportBank.log', filemode='w', level=logging.DEBUG)

filename=input('Specify filename')
# filename = filename+".csv"
option=input("Select '1' to list value in credit/debit for each employee. Select '2' to list all transactions for a given name")

def rounder(number):
    number=round(number,2)
    number=str(number)
    number_split = number.split('.')
    if len(number_split[1]) != 2:
        number = number + '0'
    return number

def sum_all(file):
    i = 0
    names = {}
    for line in file:
        debtor = line[1]
        creditor = line[2]
        if i != 0:
            try:
                val = float(line[4])
            except ValueError:
                logging.info(line[4]+" is not a valid price. Please check datafile")
                print("ERROR on line "+str(i+1)+" of file. Check the logfile for more details!")

                continue
            if debtor in names.keys():
                names[debtor] = names[debtor] - val
            else:
                names[debtor] = -val
            if creditor in names.keys():
                names[creditor] = names[creditor] + val
            else:
                names[creditor] = val
        i = i + 1
    for name in names:
        final_val=names[name]
        final_val=rounder(final_val)
        print("Account holder "+name+" has a total balance of £"+final_val)


with open(filename) as file:
    file=csv.reader(file,delimiter=',')
    if option == '1':
        sum_all(file)

    elif option == '2':
        name = input("Please give name of account holder")
        account = False
        for line in file:
            debtor = line[1]
            creditor = line[2]
            if name == debtor or name == creditor:
                account = True
                number=line[4]
                number=float(number)
                number=rounder(number)
                print("Date "+line[0]+" Debtor: "+debtor+" Creditor: "+creditor+" Narrative: "+line[3]+" Value: £"+number)
        if not account:
            print("Account does not exist!")
    else:
        print("Bad Input!")