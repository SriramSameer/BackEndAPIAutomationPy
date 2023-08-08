import csv

with open('utilities/loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile,delimiter=',')
    # print(csvReader)
    # print(list(csvReader))
    names = []
    status = []
    for row in csvReader:
        names.append(row[0])
        status.append(row[1])

print(names)
print(status)
Index = names.index('Sam')
loanStatus = status[Index]
print('Sam loan status is' +loanStatus)

with open('utilities/loanapp.csv', 'a')as wFile:
    write = csv.writer(wFile)
    write.writerow(["Bob", "rejected"])
