# Write a program to check whether a character is:
# uppercase letter
# lowercase letter
# digit
# special character

ch = input("enter a character")

if ch.isupper():
    print("uppercase letter is there")
elif ch.islower():
    print("lowercase letter is there")
elif ch.isdigit():
    print("digit is there")
else:
    print("special character")