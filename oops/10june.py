class student:
    college_name = "yahuuu college"
    
    def __init__(self,name,marks): # constructor
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print("welcome students",self.name)
        
    def get_marks(self):
        return self.marks
    
s1 = student("seeta",90)
s1.welcome()
print(s1.get_marks())
            