import csv
import sys

option=input("Select '1' to list value in credit/debit for each employee. Select '2' to list all transactions for a given name")
if option == '1':
    with open('Transactions2014.csv') as file:
        i=0
        names={}
        file=csv.reader(file,delimiter=',')
        for line in file:
            debtor=line[1]
            creditor=line[2]
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

