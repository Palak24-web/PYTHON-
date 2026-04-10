# Write a program to find the middle number among three different numbers.
 
a = int(input("enter 1st number:")) 
b = int(input("enter 2nd number:")) 
c = int(input("enter 3rd number:")) 

if (a>b and a<c) or (a<b and a>c):
    print("middle no is:",a)
    
elif (b>a and b<c) or (b<a and b>c):
    print("middle no is:",b)
    
else:
    print("middle no is:",c)
    