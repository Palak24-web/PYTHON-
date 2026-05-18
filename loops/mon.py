# Check whether a number is a palindrome using a loop.

n = int(input("enter a number:"))

original = n
rev = 0

while n>0:
    digit = n % 10  # if we give 123 so 123 % 10 i.e = 3
    rev = rev * 10 + digit  # 0 +3  i.e=3  multiplying by 10 shifts the digit to the left that makes space for the new digit at the right
    n = n//10
    
if original==rev:
       print("palindrome number")
else:
       print("not a palindrome") 