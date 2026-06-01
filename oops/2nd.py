class complex:
    def __init__(self,real,img):
        self.real = real
        self.img= img
        
    def shownumber(self):
        print(self.real,"i+",self.img,"j")
        
    def __add__(self,another):
        newreal = self.real + another.real
        newimg = self.img + another.img
        return complex(newreal,newimg)
    
num1 = complex(5,5)
num1.shownumber()

num2 = complex(8,6)
num2.shownumber()

num3 = num1+num2
num3.shownumber()            