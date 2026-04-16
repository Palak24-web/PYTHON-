# Write a program to check whether a number is Armstrong (3-digit).

num = int(input("enter a 3 digit number:"))

temp = num
sum_cubes=0

while temp >0:
    digit = temp % 10 # extract last digit
    sum_cubes = sum_cubes + (digit ** 3)
    temp = temp // 10 # removes last digit move to next digit

if sum_cubes == num:  # check if the sum of the cubes is = original number
     print("armstrong number")
else:
     print("not a armstrong num")