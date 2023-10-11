val = int(input("Enter a value:"))
temp = val
count = 0
while val >= 1:
    count = count + 1
    val = int(val / 10)
sum = 0
num = temp
while temp >= 1:
    digit = int(temp % 10)
    sum = sum + digit ** count
    temp = int(temp / 10)
if sum == num:
    print("The number ", num, "is an armstrong number")
else:
    print("The number ", num, "is not an armstrong number")