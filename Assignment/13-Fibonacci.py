lst = []

a = 0
b = 1

for i in range(0, 11):
    lst.append(a)
    c = a + b
    a = b
    b = c

print(lst)

for i in lst:
    lstEven = filter(lambda i: i % 2 == 0, lst)
    lstOdd = filter(lambda i: i % 2 != 0, lst)

print(list(lstEven))
print(list(lstOdd))