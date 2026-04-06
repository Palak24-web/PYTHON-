# Take a number and check:
# divisible by 4 but not by 6
# divisible by 6 but not by 4
# divisible by both
# divisible by none

h = int(input("enter a number:"))

if h%4==0 and h%6!=0:
    print("divisible by 4 but not by 6")
    
elif h%6==0 and h%4!=0:
    print("divisible by 6 but not by 4")
elif h%4==0 and h%6==0:
    print("divisible by both")
else:
    ("divisible by none")