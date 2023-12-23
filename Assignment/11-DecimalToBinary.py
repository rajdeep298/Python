binary = []

decimal = int(input("Enter a decimal number: "))

while decimal >= 1:
    binary.append(decimal % 2)
    decimal = int(decimal / 2)

binary.reverse()
for i in binary:
    print(i, end="")
