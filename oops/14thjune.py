class student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
            print("🙋🏻‍♂️",self.name,"your avg  score is:",sum/3)
            
     
s1 = student("hariom", [45,90,79])
s1.get_avg()

s1.name = "shree"
s1.get_avg()