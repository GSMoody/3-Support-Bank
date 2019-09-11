import csv
import sys

option=input("Select '1' to list value in credit/debit for each employee. Select '2' to list all transactions for a given name")


def sum_all(file):
    i = 0
    names = {}
    for line in file:
        debtor = line[1]
        creditor = line[2]
        if i != 0:
            val = float(line[4])
            if debtor in names.keys():
                names[debtor] = names[debtor] - val
            else:
                names[debtor] = -val
            if creditor in names.keys():
                names[creditor] = names[creditor] + val
            else:
                names[creditor] = val
        i = i + 1
    print(names)


with open('Transactions2014.csv') as file:
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
                print("Date "+line[0]+" Debtor: "+debtor+" Creditor: "+creditor+" Narrative: "+line[3]+" Value: £"+line[4])
        if not account:
            print("Account does not exist!")
    else:
        print("Bad Input!")

x = 1 == 1


