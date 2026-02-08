# Check if a string is a palindrome.

s = input("enter a string:")
 
reverse = ""

for i in s:
    reverse = i + reverse

if s == reverse :
    print ("palindrome")
    
else:
    print("not palindrome")    