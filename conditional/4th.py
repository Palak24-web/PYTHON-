marks1 = int(input("enter marks 1:"))
marks2 = int(input("enter marks 2:"))
marks3 = int(input("enter marks 3:"))

#check for total percentage

total_percantage = (marks1 + marks2 + marks3)/3

if(total_percantage >= 90):
    print ("A grade")

elif(total_percantage >= 40):
    print("ur pass", total_percantage)

else:
     print("better luck for next time")