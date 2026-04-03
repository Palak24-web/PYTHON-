# A shop gives discounts — write code to calculate final bill.

amount=int(input("enter amount of final bill"))
 
if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.10
else:
    discount=0
    
final_amount= amount - discount
print("final bill amount :", final_amount)
     
     