class student:
    
    def __init__(self,name,marks):
        self.name=name 
        self.marks = marks
        
    @staticmethod  # decorator 
    def welcome(): 
        print("hlo wlcome to the class")
        
s1 = student("priya",65) 
student.welcome()            