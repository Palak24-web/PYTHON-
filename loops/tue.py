# Find the GCD of two numbers using a loop.

a = int(input("enter 1st number:"))
b = int(input("enter 2nd number:"))

gcd =1

for i in range(1,min(a,b)+1):
    if a%i==0 & b%i==0:
        gcd = i

print(gcd)        