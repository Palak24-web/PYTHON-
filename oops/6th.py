class complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def shownumber(self):
        print(self.real,"i+",self.imaginary,"j")
        
num1 = complex(5,6) 
num1.shownumber()

num2 = complex(6,22)
num2.shownumber()