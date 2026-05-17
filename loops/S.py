# Find the sum of digits of a number using a loop.

n = int(input("enter digits"))

sum = 0

while n>0:
     digit = n % 10  # gives the last digit of the number
     sum = sum + digit
     n=n//10 # removes the last digit

print(sum)     
     