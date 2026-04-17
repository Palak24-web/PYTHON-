# Write a menu-driven program:
# 1 → check even/odd
# 2 → check prime
# 3 → find factorial
# 4 → exit -->

print("1.check even or odd")
print("2.check prime")
print("3.check factorial")
print("4.exit")

choice = int(input("enter ur choice:"))

if choice==1:
    num = int(input("enter a number"))
    if num%2==0:
        print("even number")
    else:
        print("odd number")
        
elif choice==2:
    num = int(input("enter a number"))
    if num<=1:
        print("not prime")
    else:
        for i in range(2,num):
            if num%2==0:
                print("not prime")
                break
            else:
                print("prime number")
                
elif choice==3:
    num = int(input("enter a number"))
    fact = 1
    
    for i in range(1,num+1):
        fact = fact*i
        
        print("fact")

elif choice==4:
    print("exit program")
    
else:
    print("invalid choice")    
                                       
    
        