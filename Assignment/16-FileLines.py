import sys

fileName = sys.argv[1]

fp = open(fileName, "r")

try:
    lines = fp.readlines()
    lineNo = len(lines)
    print("Total number of lines in the file: ", lineNo)
except FileNotFoundError:
    print("File not found")
