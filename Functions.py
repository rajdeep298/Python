# Lambda function
#  is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax: lambda arguments : expression
square = lambda x: x * x
print(square(5))

# Filter function
# The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
# Syntax: filter(function, iterables)
numbers = (1, 2, 3, 4, 5)
evenNumbers = list(filter(lambda x: x % 2 == 0, numbers))
print(evenNumbers)

# Map function
# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
# Syntax: map(function, iterables)
numbers = (1, 2, 3, 4, 5)
squareNumbers = list(map(lambda x: x * x, numbers))
print(squareNumbers)
