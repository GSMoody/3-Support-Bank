import csv

option=input("Select '1' to list value in credit/debit for each employee. Select '2' to list all transactions for a given name")
if option == '1':
    results=[]
    with open('Transactions2014.csv') as file:
        i=0
        names={}
        file=csv.reader(file,delimiter=',')
        for line in file:
            #print(file)
            if i != 0:
                if line[1] not in names:
                    names.append(line[1])
                if line[2] not in names:
                    names.append(line[2])
            i = i +1
        print(names)
        for name in names:
            print(name)
            debt=0.0
            credit=0.0
            #print(file)
            for line in file:
                print(line)
                if name == line[1]:
                    debt=debt+float(line[4])
                elif name == line[2]:
                    credit=credit+float(line[4])
            sum=credit-debt
            #print(name+"'s total balance is £"+str(sum))

