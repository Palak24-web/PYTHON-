# Check whether a number is prime using a loop.
n = int(input("enter a number:"))

if n<=1:
    print("not a prime no")
else:
    prime = True   # asuume the number is prime
    
    
    for i in range(2,n):
        if n % i == 0: 
           prime = False  # number is not prime
           break
        
    if prime:
         print("prime number")
    else:
         print("not prime")