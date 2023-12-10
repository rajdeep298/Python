string1='Rajdeep'
string2="Rajdeep" #both are same
print(string1)
print(string2)

# Multiline string
string3='''Hello
            World'''
print(string3)

# Accessing characters in a string
print(string1[0])
print(string1[1])
print(string1[2])
print(string1[3])
print(string1[4])
print(string1[5])
print(string1[6])
print()

# Accessing characters in a string from the end
print(string1[-1])
print(string1[-2])
print(string1[-3])
print(string1[-4])
print(string1[-5])
print(string1[-6])
print(string1[-7])

# Slicing
print(string1[0:3])
print(string1[3:6])
print(string1[0:6])
print(string1[:6])
print(string1[0:])
print(string1[:])

#Slicing with step
print(string1[0:7:2])
print(string1[::-1]) #reverse string

# String concatenation
print(string1+string2)

# String repetition
print(string1*3)

# String length
print(len(string1))

# String membership
print('Raj' in string1)

# Raw string
RawString=r'Hello\nWorld' #it treats backslashes as literal character
print(RawString)

# String formatting using format operator
print("My name is {}".format(string1))

# String formatting using % operator
print("My name is %s" % string1)

# String formatting using f-strings
print(f"My name is {string1}")

# Count method
print(string1.count('e'))# returns the number of occurrences of substring in string

# Find method
print(string1.find('e'))# returns the index of first occurrence of substring in string

# Replace method
print(string1.replace('e','i'))# returns a copy of string with all occurrences of substring old replaced by new

# Split method
print(string1.split('e'))# returns a list of all the words in the string, using str as the separator

# Strip method
string3='    Hello    '
print(string3)
print(string3.strip())# returns a copy of the string with the leading and trailing characters removed

# Upper method
print(string1.upper())# returns a copy of the string converted to uppercase

# Lower method
print(string1.lower())# returns a copy of the string converted to lowercase

