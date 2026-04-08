# Take three sides of a triangle and check:
# whether a triangle is possible
# if possible, check whether it is equilateral, isosceles, or scalene

a = int(input("enter 1st side"))
b = int(input("enter 2nd side"))
c = int(input("enter 3rd side"))

if a+b>c and b+c>a and a+c>b:
    print("yes triangle")
    if a==b==c:
        print("it's a equilateral traingle")
    elif a==b or b==c or a==c:
        print("isosceles triangle")
    else:
        print("scalene triangle")
        
else:
    print("not a triangle")        