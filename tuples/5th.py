# Take a tuple of strings and:
# count how many strings have length greater than 5

t = ("ok","greatest","how","areeeyyy","u")

count=0
for i in t:
    if len(i)>5:
     count +=1
     
print(count)     