# Count the vowels in a string.

x = input("enter a string:")

vowels = "aeiouAEIOU"
count = 0

for i in x:
    if i in vowels:
        count += 1

print(count)        