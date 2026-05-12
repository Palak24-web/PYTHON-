# .Print Fibonacci series up to n terms. 
n = int(input("enter number of terms="))
a = 0
b = 1

# print(a)

for i in range(n):
    print(a)  # starting with 0
    next = a+b  
    # print(next)
    a=b  # update the value 
    b=next  # go for the next value
    