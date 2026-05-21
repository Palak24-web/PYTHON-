# Find the largest element in a list using a loop.

lst = ["😏😏😏","💕💕","🤟🏻🤣👽👻🎮","hehe"]

largest = lst[0]  # assuming 1st element as largest

for i in lst:
    if i>largest: # compare with others and update
        largest = i
print(largest)            