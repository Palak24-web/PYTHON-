class student:
    college_name = "hehe college"
    name_student = "ram" # class atrribute used for all objects as a default value 
    
    def __init__(self,name,marks):
        self.name = name # instance or object attribute >>> class attribute 
        self.marks = marks
        print("addding new student databse:")
        
s1 = student("ohkkk",90)
print(s1.name,s1.marks)        