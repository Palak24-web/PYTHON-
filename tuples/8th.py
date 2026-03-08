# Replace an element at a given index in a tuple
# (Hint: tuples are immutable)

t = (1,2,3,4,5,6)

index=int(input("enter index to replace"))
new_value=int(input("enter new value"))

lst=list(t)
lst[index]=new_value
t=tuple(lst)
print(t)
