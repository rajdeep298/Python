#Packing Lists into Tuples
my_list = [1, 2, 3]
var1,var2,var3 = my_list# var1=1,var2=2,var3=3
my_tuple = (var1,var2,var3)
print(my_tuple) # Output: (1, 2, 3)

#Extended Unpacking
my_list = [1, 2, 3, 4, 5, 6]
a, *b, c = my_list # a=1,b=[2,3,4,5],c=6
print(a) # Output: 1
print(b) # Output: [2, 3, 4, 5]
print(c) # Output: 6

#Slicing Tuples
my_tuple = (1, 2, 3, 4, 5, 6)
print(my_tuple[0:3]) # Output: (1, 2, 3)
print(my_tuple[3:6]) # Output: (4, 5, 6)
print(my_tuple[0:6:2]) # Output: (1, 3, 5)
print(my_tuple[::-1]) # Output: (6, 5, 4, 3, 2, 1)