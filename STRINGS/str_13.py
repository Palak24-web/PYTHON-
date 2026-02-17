# Replace every vowel in a string with "*"

a = input("enter a string:")
result = ""

for ch in a:
    if ch in "aeiouAEIOU":
        result+="*"
        
    else:
        result+=ch

print(result)            