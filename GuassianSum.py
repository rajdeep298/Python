n=int(input("Enter the number of elements: "))

list1=[]
list2=[]

for i in range(0,n):
    num=int(input("Enter the number: "))
    list1.append(num)


for i in range(0,int(n/2)):
    sum=list1[i]+list1[n-i-1]
    list2.append(sum)

lenList2=int(len(list2))

sum=0

for i in range(0,lenList2):
    sum=sum+list2[i]

print("The sum of the elements of the new list is: ",sum)