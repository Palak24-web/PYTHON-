# Grade a student based on marks using if-elif.

marks = int(input("enter marks of a student:"))

if marks>=90:
    print("A grade")
elif marks>=80:
    print("B grade")
elif marks >= 60:
    print("C grade")
elif marks == 40:
    print("passed only")
else:
    print("oops failed")