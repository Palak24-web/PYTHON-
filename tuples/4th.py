# Create a tuple of 6 numbers and:
# print only even numbers from it
 
# t=(1,2,3,4)
# lst = list(t)
# lst.append(4)
# t=tuple(lst)
# print(t) 

t = (1,2,4,5,6,7)

print("even numbers:")
for i in t:
  if i % 2==0 :
    print(i)
