# using try and except to handle errors

# ZeroDivisionError
# This happens when you try to divide by zero
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# FileNotFoundError
# This happens when you try to open a file that does not exist
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("Sorry, the file " + filename + " does not exist.")

# ValueError
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number.lower() == 'q':
        break
    second_number = input("Second number: ")
    if second_number.lower() == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ValueError:
        print("You must enter a number!")
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

# TypeError
try:
    print('5' + 5)
except TypeError:
    print("Can't add string and integer together")

# IndexError
try:
    x = [1, 2, 3]
    print(x[3])
except IndexError:
    print("Index out of range")

# KeyError
try:
    x = {'a': 1, 'b': 2}
    print(x['c'])
except KeyError:
    print("Key not found")

# AttributeError
try:
    x = 5
    x.append(1)
except AttributeError:
    print("Attribute not found")

# and so on...
