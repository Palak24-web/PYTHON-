class car:
    @staticmethod
    def start():
        print("car started")
        
    @staticmethod
    def stop():
        print("car stopped")
        
class toyotacar(car):
     def __init__(self,model):
         self.model =model
         
class bmw(toyotacar):
      def __init__(self,name):
          self.name = name

car1 = bmw("superninja")
print(bmw.start())   
# print(car1.name)                           
print(toyotacar.__name__)