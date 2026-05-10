# Find the factorial of a number using a loop.
num = int(input("enter a number="))
fact = 1
for i in range(1,num+1):
    fact = fact*i
print(fact)    