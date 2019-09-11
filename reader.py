import csv
import json
import sys
import logging
import re
import datetime

logging.basicConfig(filename='SupportBank.log', filemode='w', level=logging.DEBUG)

#filename=input('Specify filename')
filename='Transactions2013.json'
filetype=filename.split(".")[-1]
option=input("Select '1' to list value in credit/debit for each employee. Select '2' to list all transactions for a given name")

def rounder(number):
    number=round(number,2)
    number=str(number)
    number_split = number.split('.')
    if len(number_split[1]) != 2:
        number = number + '0'
    return number

def sum_all(file,to_index,from_index,val_index):
    names = {}
    i=1
    for line in file:
        debtor = line[from_index]
        creditor = line[to_index]
        try:
            val = float(line[val_index])
        except ValueError:
            logging.info(line[val_index]+" is not a valid price. Please check datafile")
            print("ERROR on line "+str(i+1)+" of '"+filename+"'. Check the logfile for more details!")
            continue
        if debtor in names.keys():
            names[debtor] = names[debtor] - val
        else:
            names[debtor] = -val
        if creditor in names.keys():
            names[creditor] = names[creditor] + val
        else:
            names[creditor] = val
        i=i+1
    for name in names:
        final_val=names[name]
        final_val=rounder(final_val)
        print("Account holder "+name+" has a total balance of £"+final_val)


with open(filename) as file:
    if filetype == 'json':
        file = json.load(file)
        header=[]
        for key in file[0]:
            header.append(key.lower())
    elif filetype == 'csv':
        file=csv.reader(file,delimiter=',')
        top_row=next(file)
        header=[]
        for word in top_row:
            header.append(word.lower())
    i=0
    for word in header:
        if 'date' in word:
            date_index=i
        elif 'to' in word:
            to_index=i
        elif 'from' in word:
            from_index=i
        elif 'narrative' in word:
            note_index=i
        elif 'amount' in word:
            val_index=i
        i=i+1
    print(header)
    print(date_index,to_index,from_index,note_index,val_index)
    print(file)
    for line in file:
        print(line)
    sys.exit()
    if option == '1':
        sum_all(file,to_index,from_index,val_index)

    elif option == '2':
        i=1
        name = input("Please give name of account holder")
        account = False
        for line in file:
            debtor = line[from_index]
            creditor = line[to_index]
            if name == debtor or name == creditor:
                account = True
                number=line[val_index]
                number=float(number)
                number=rounder(number)
                try:
                    datetime.datetime.strptime(line[date_index],"%d/%m/%Y")
                except ValueError:
                    print("DATE ON LINE "+str(i)+" IS NOT IN DD-MM-YYYY FORMAT!!")
                    logging.info(line[date_index]+"on line "+str(i)+" is not a valid date format.")
                print("Date "+line[date_index]+", Debtor: "+debtor+", Creditor: "+creditor+", Narrative: "+line[note_index]+", Value: £"+number)
            i=i+1
        if not account:
            print("Account does not exist!")
    else:
        print("Bad Input!")