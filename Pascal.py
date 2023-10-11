def main():
    n=int(input("Enter the number of lines: "))
    pascal(n)

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def pascal(n):
    for i in range(n):
        for j in range(n-i):
            print(" ",end=" ")
        for j in range(i+1):
            print(int(factorial(i)/(factorial(j) *factorial(i-j))),end=" ")
        print()

if __name__=='__main__':
    main()