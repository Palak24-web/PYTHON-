# Check if a password is strong (conditions: len>8, number, special char).

password = input("enter a password:")

if (len(password)>8 and any(ch.isdigit() for ch in password) and any(ch in "!@#$%&" for ch in password)):
 print("strong password")
else:
 print("weak password")