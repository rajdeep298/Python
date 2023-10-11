n=int(input("Enter the number of terms: "))

a=2
b=1

for i in range(0,n):
    if i%2==0:
        print(a,end=",")
        a=a+2
    else:
        print(b,end=",")
        b=b+2