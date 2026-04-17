# Write a program to check whether a number is Strong number.
num = int(input("enter a 3 digit number:"))

temp = num
factorial_sum = 0

while temp>0:
    digits = temp % 10
    
    fact = 1
    for i in range(1,digits+1):
        fact = fact * i
        
    factorial_sum = factorial_sum + fact
    temp = temp//10
                   
if factorial_sum == num :
     print("strong number")
else:
     print("not a strong num")    