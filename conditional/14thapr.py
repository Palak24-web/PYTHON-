# Write a program to check whether a number is:
# negative odd
# negative even
# positive odd
# positive even

number= int(input("enter a number:"))

# number = 0

if number > 0 and number %2 ==0:
    print("postive even number")
elif number < 0 and number %2!= 0:
    print("negative  odd number")
elif number > 0 and number % 2 !=0:
    print("postive odd number")
elif number < 0 and number % 2==0:
    print("negative even number")
else:
    print("undefined")
        