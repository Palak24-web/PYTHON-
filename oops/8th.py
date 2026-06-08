class car:
    colour = "black"
    @staticmethod
    def start():
        print("car strted..")
    
    @staticmethod
    def stop():
        print("car stopped..")
        
class bmw(car):
    def __init__(self,name):
        self.name = name
        # self.colour = colour
        
car1 = bmw("X5")
car2 = bmw("X3")

print(car1.name)     
print(car1.start())           
print(car1.colour)