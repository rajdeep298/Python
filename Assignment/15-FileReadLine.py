import sys

fileName = sys.argv[1]

fp = open(fileName, "r")
if fp == None:
    print("File not found")
    exit(0)

n = int(input("Enter the number of lines to read: "))

lines = fp.readlines()
print(lines[0:n])

print(lines[len(lines):n-1:-1])
