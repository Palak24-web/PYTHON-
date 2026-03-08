# Find the second largest element in a tuple. 

t = (10,20,30,40)

max1=t[0]
max2=t[0]

for i in t:
    if i > max1:
        max2=max1
        max1=i
    elif i < max1 and i>max2 and i!=max1:
        max2=i
print("2nd largest:",max2)        
        