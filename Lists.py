# Nested Lists
List1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(List1)

# Accessing elements in a nested list
print(List1[0])  # first sub-list
print(List1[0][0])  # first element of first sub-list

# Slice a nested list
print(List1[0:2])  # first two sub-lists #Output: [[1, 2, 3], [4, 5, 6]]
print(List1[0][0:2])  # first two elements of first sub-list #Output: [1, 2]

# List comprehension
List2 = [i for i in range(10)]
print(List2)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

List3 = [i for i in range(10) if i % 2 == 0]
print(List3)  # Output: [0, 2, 4, 6, 8]

List4 = [i for i in range(10) if i % 2 != 0]
print(List4)  # Output: [1, 3, 5, 7, 9]

# List comprehension with nested list
List5 = [[i for i in range(3)] for j in range(3)]
print(List5)  # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

List6 = [[i for i in range(3)] for j in range(3) if j % 2 == 0]
print(List6)  # Output: [[0, 1, 2], [0, 1, 2]] prints only sub-lists when j is even

List7 = [[i for i in range(3)] for j in range(3) if j % 2 != 0]
print(List7)  # Output: [[0, 1, 2], [0, 1, 2]] prints only sub-lists when j is odd

# Iterating through a nested list
for i in List1:  # iterate through each sub-list
    print(i, end='\t')
print()

for i in List1:  # iterate through each element
    for j in i:
        print(j, end='\t')
    print()

# Append

# apppend a list
List2.append(10)  # append 10 at the end of the list
print(List2)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10]
# append a nested list
List1.append([10, 11, 12])  # append a list at the end of the list
print(List1)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10,11,12]]

# Extend
List2.extend(List3)  # extend the list by appending all the items from the iterable
print(List2)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10, 0, 2, 4, 6, 8]
List3.extend("Hello")  # extend the list by appending all the items from the iterable
print(List3)  # Output: [0, 2, 4, 6, 8, 'H', 'e', 'l', 'l', 'o'] reading hello by characters

# Insert
List2.insert(0, 0)  # insert an item at a given position
print(List2)  # Output: [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10, 0, 2, 4, 6, 8]

# Remove
List2.remove(0)  # remove the first item from the list whose value is 0
print(List2)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10, 0, 2, 4, 6, 8]

# Pop
List2.pop()  # remove the last item from the list
print(List2)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10, 0, 2, 4, 6]

# Clear
List2.clear()  # remove all items from the list
print(List2)  # Output: []

# Split
string1 = "Hello World"
List8 = string1.split(" ")  # split a string into a list
print(List8)  # Output: ['Hello', 'World']
