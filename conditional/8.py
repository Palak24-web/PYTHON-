marks = int(input("enter ur marks="))

if(marks<=100 and marks>90):
    print("grade A")

elif(marks<=90 and marks>80):
        print("very good")
elif(marks<=80 and marks>70):
        print("good")
elif(marks<=70 and marks>60):
        print("fair")
elif(marks<=60 and marks>50):
        print("passed")
else:
    print("keep trying")