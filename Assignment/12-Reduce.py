from functools import reduce

max_find = lambda a, b: a if (a > b) else b

print("Enter the number of elements in the list")
n = int(input())
print("Enter the elements of the list")
l = []
for i in range(n):
    l.append(int(input()))
print("The maximum element in the list is", reduce(max_find, l))
