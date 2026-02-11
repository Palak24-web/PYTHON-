# Remove all special characters from a string

a = input("enter a string:")
special_characters = "!@#$%&*"
result = ""

for i in a:  # checks each character starting from the i=0
    if i not in special_characters:
       result += i
       
print(result)     