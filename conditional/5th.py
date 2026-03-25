Q1= "Make a lot of money"
Q2 = " buy now"
Q3 = " subscribe this"
Q4= "click this"

msg = input("enter ur msg:")

if(Q1 in msg or Q2 in msg or Q3 in msg or Q4 in msg):
    print("this is a spam")

else:
 print("this is not a spam")