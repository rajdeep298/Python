val1 = int(input("Enter a value:"))
val2 =int(input("Enter another value:"))
add = val1 + val2
print("Addition:", add)
sub = val1 - val2
print("Substractions:", sub)
mult = val1 * val2
print("Multiplication:", mult)
div = val1 / val2
print("Division:", div)

def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,int(a%b))

gcd= GCD(val1,val2)
print("GCD:",gcd)