class account:
    def __init__(self,bal,acc):
        self.bal = bal
        self.acc_no  = acc
    
    #debit method
    def debit(self , amount):
        self.bal -=amount
        print("Rs.",amount,"was debited")
        
    def credit(self , amount):
        self.bal += amount
        print("Rs.",amount,"was credited")  
        
    def get_balance(self):
        return self.bal         


acc1 = account(229999,4323234)
acc1.debit(1000)
acc1.credit(12345)

acc1.credit(20000)
acc1.debit(2345)

print("total balance is: Rs.",acc1.get_balance())