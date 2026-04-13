# Take age and gender:
# male ≥ 21 → eligible for marriage
# female ≥ 18 → eligible for marriage

a = int(input("enter age of a person:"))
b = input("enter gender (male/female)=")

if b=="male" and a >=21:
    print("eligible for marriage")
    
elif b=="female" and a>=18 :
        print("eligible for marriage")
        
else:
        print("not eligible ")


    