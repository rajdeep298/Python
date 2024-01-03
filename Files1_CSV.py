import csv

data = [['Name', 'Age', 'Phone'], ['John', 25, 1234567890], ['Jane', 30, 9876543210]]

# read the file
datafile = open('Input.csv', 'r')
datareader = csv.reader(datafile, delimiter=',')
for row in datareader:
    print(row)
datafile.close()

# Write to the file
datafile = open('Output.csv', 'w')
datawriter = csv.writer(datafile, delimiter=',')
datawriter.writerows(data)
datafile.close()

# Delimiter
datafile = open('Output.csv', 'w')
datawriter = csv.writer(datafile, delimiter='|')
datawriter.writerows(data)
datafile.close()

# Quote Character
datafile = open('Output.csv', 'w')
datawriter = csv.writer(datafile, delimiter=',', quotechar='"')
datawriter.writerows(data)
datafile.close()

# DictReader
datafile = open('Input.csv', 'r')
datareader = csv.DictReader(datafile, delimiter=',')
for row in datareader:
    print(row)
datafile.close()

# DictWriter
data = [
    {'Name': 'John', 'Age': 28, 'Phone': 1234567890},
    {'Name': 'Alice', 'Age': 22, 'Phone': 9876543210},
    {'Name': 'Bob', 'Age': 32, 'Phone': 1231231230}
]
datafile = open('Output.csv', 'w')
datawriter = csv.DictWriter(datafile, delimiter=',', fieldnames=['Name', 'Age', 'Phone'])
datawriter.writeheader()
datawriter.writerows(data)
datafile.close()
