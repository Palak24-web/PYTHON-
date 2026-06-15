class person:
    __name = "😁💕" # class internal functions can access it outside the class no one can access it
    
    def __hello():
        print("hello person")
        
    def welcome(self):
        __hello()     # can be accessed becoz its inside the class
        
p1 = person()

print(p1.__hello())        