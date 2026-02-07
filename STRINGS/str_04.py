# Replace all spaces in a string with "_"

a = input("enter a string:")
result = ""

for i in a:
    if i == " ":
        result += "_"
        
    else:
        result += i
        
print(result)        