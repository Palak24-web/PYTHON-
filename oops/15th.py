# class account:
#     def __init__(self,acc_no,pass):
#         self.acc_no=acc_no
#         self.pass = pass
        
# acc1  = account("12345","kdh23")

# print(acc1.acc_no)
# print(acc1.pass)   #this can be accessed by anyone becoz this is public variable 
#to make it private we use __ before variable name 

class account:
    def __init__(self,acc_no,__pass):
        self.acc_no = acc_no
        self.__pass = __pass  # private variable
        
acc1 = account("12345","hnn7")
print(acc1.acc_no)
# print(acc1.__pass)        
# this will give an error becoz __pass is a private variable and can't be accessed directly