class student:
    def __init__(self,accounts,business,economics):
        self.accounts = accounts
        self.business = business
        self.economics = economics
        
    @property
    def percentage(self):
      return str((self.accounts + self.business + self.economics) /3 ) + "%"
        
stud1 = student(34,89,67)
print(stud1.percentage)
        
stud1.economics = 90
print(stud1.percentage)        