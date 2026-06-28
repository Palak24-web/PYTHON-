class employee:
    company = "TCS"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")

# class programmer:
#     company = "fiverr"
#     def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")

#         def showlanguage(self):
#             print(f"the language is {self.name} and he is good in {self.language} language") 

# instead of creating so many classes we can use inheritance

class programmer(employee):
    company = "fiverr"
    def showlanguage(self):
        print(f" the name is {self.name} and the language is {self.language}")

a=employee()
b=programmer()

print(a.company,b.company)