lst1 = ["Apple", "Banana", "Cherry", "Orange", "Kiwi", "Mango"]
lst2 = ["Dog", "Cat", "Rat", "Lion", "Tiger", "Elephant"]

print(lst1)
print(lst2)

lstEven = lst1[::2]
lstOdd = lst2[1::2]

lstEven = ",".join(lstEven)
lstOdd = ",".join(lstOdd)

print(lstEven)
print(lstOdd)
