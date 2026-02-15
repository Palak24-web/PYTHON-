# Split a full name into first name and last name.
name = input("enter a full name")

parts=name.split() # breaks the string whenever there is a space

first_name = parts[0]
last_name = parts[-1]  # -1 for the last word of that sentence or name

print("first_name=",first_name)
print("last_name=",last_name)

