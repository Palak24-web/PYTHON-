# Take a string input and print it in reverse.

x = input("enter a string:")

reverse =""
for i in x:
    reverse = i+reverse
    
print(reverse) 