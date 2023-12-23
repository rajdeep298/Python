a=int(input("Enter the coefficient of x^2: "))
b=int(input("Enter the coefficient of x: "))
c=int(input("Enter the constant: "))

x1=((-b)+((b**2)-(4*a*c))**0.5)/(2*a)
x2=((-b)-((b**2)-(4*a*c))**0.5)/(2*a)

print("The roots of the quadratic equation are: ",x1,"and",x2)