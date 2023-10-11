lst=['apple','banana','mango']
print(lst)

lst.append('guava')
print(lst)

lst[2]='pomegranate'
print(lst)

lst.remove('banana')
print(lst)

if any(fruit=='mango' for fruit in lst):
    print("Mango is present in the lst")
else:
    print("Mango is not present in the lst")

# if list.count('mango') > 0:
#     print("Mango is present in the lst")
# else:
#     print("Mango is not present in the lst")

# x = lst.find('mango')
# print(x)

# x= list.count('mango')
# print(x)
