class car:
    def __init__(self,name):
        self.name = name
        
    @staticmethod
    def start():
        print("car started")
            
    @staticmethod             
    def stop():
        print("car stopped")
            
class tata(car):
    def __init__(self,name,type):
        super().__init__(name)
        self.type = type
        super().start()
        
c1 = tata("nexon","suv")
print(c1.name)
print(c1.type)
