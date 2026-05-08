# Find the sum of first n natural numbers using a loop.

num = int(input("enter num:"))

sum=0
for i in range(1,num+1): # each no from 1 to n is added
    sum = sum+i
   
print(sum)    
    