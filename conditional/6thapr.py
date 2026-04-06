# Print whether a number is single-digit, double-digit, or more.
a  = int(input("enter a number"))

a = abs(a) # absolute value of a that removes - sign 

if a < 100:
    print("double digit")
elif a<10:
    print("single digit")
else:
    print("more than two digits")