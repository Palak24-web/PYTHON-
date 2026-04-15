# Write a program to check whether a number is a Harshad number.

num = int(input("enter number="))

sum_digits = 0
temp = num   #copy a number so original value is save

while temp >0:
    digit = temp % 10 # extract last digit
    sum_digits=sum_digits+digit
    temp = temp // 10 # removes last digit

if num % sum_digits == 0:
     print("harshad num")
else:
     print("not a harshad num")