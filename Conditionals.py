#Containment checking
my_tuple = (1, 2, 3, 4, 5, 6)
print(1 in my_tuple) # Output: True
print(7 in my_tuple) # Output: False
print(1 not in my_tuple) # Output: False

my_list = [1, 2, 3, 4, 5, 6]
print(1 in my_list) # Output: True
print(7 in my_list) # Output: False
print(1 not in my_list) # Output: False

my_string = "Rajdeep"
print('R' in my_string) # Output: True
print('r' in my_string) # Output: False
print('R' not in my_string) # Output: False

my_dict = {1: 'a', 2: 'b', 3: 'c'}
print(1 in my_dict) # Output: True
print(7 in my_dict) # Output: False
print(1 not in my_dict) # Output: False

my_set = {1, 2, 3, 4, 5, 6}
print(1 in my_set) # Output: True
print(7 in my_set) # Output: False
print(1 not in my_set) # Output: False