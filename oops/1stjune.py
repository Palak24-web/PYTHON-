class car:
    def __init__(self):
        self.acc = False
        self.brk = False # false means not pressed
        
    def start(self):
        self.acc = True
        self.brk = True
        print("car is started..")
        
car1 = car()
car1.start()            