# 3.Check whether a tuple is a palindrome.

t = input("enter a tuple:")

if t == t[::-1]:
    print("tuple is a palindrome")
else:
    print("tuple is not a palindrome")