#copying content of one file to another file
import sys

n=int(input("Enter 1 for write and 2 for append: "))

ch='y'

while ch=='y':
    if n==1:
        fp1 = open(sys.argv[1], 'r')
        fp2 = open(sys.argv[2], 'w')

        for line in fp1:
            fp2.write(line)

        fp1.close()
        fp2.close()
    if n==2:
        #concatenating two files
        fp1 = open(sys.argv[1], 'r')
        fp2 = open(sys.argv[2], 'r')
        fp3 = open(sys.argv[3], 'a')

        for line in fp1:
            fp3.write(line)

        for line in fp2:
            fp3.write(line)

    ch=input("Do you want to continue? y/n: ")
    ch=ch.lower()
    fp3.close()

fp1.close()
fp2.close()
