# Count the number of digits in a given number.

count = 0
num = int(input("enter digits"))
while num>0: #loop runs until becomes 0 
    count+=1
    num = num//10 # removes the last digit

print(count)    

