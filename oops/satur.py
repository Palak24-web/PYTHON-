# def remove(l,word):
#     for item in l:
#         l.remove(word)
#         return l

# l={"radhe","mohan","geeta","seeta","eta"}
# print(remove(l,"eta"))

# or we also have to strip at the same time means remove eta from every string in the list


def remove(l,word):
        n=[]
        for item in l:
         if not(item==word):
            n.append(item.strip(word))
        return n

l={"radhe","mohan","geeta","seeta","eta"}
print(remove(l,"eta"))
