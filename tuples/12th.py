# Create a tuple of numbers and rotate it to the right by 1 position.
t = (1,2,3,4,5,6)

rotated = t[-1:]+t[:-1]  # -1:=starts from last element and "-1= except last element"

print("right rotated:",rotated)