# Write a program for ATM transaction:
# ask balance and withdrawal amount
# withdrawal allowed only if:
# amount is multiple of 100
# amount ≤ balance

balance = int(input("enter account balance:"))
amount = int(input("enter withdrawal amount="))

if amount % 100 == 0 and amount<=balance:
    balance = balance-amount
    
    print("withdrawal successfull")
    print("remaining amount:", balance)
else:
    print("something went wrong , transaction failed")
    