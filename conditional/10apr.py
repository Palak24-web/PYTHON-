# Write a program to calculate electricity bill:
# first 100 units → ₹2/unit
# next 100 units → ₹3/unit
# above 200 units → ₹5/unit

units = int(input("enter electricity units:"))

if units <= 100:
     bill = units*2
elif units <= 200:
     bill = (100*2)+(units-100)*3
else:
     bill = (100*2)+(100*3)+(units-200)*5
     
print("electricity bill is:",bill)     