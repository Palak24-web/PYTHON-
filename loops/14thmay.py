# Count how many vowels are present in a string using a loop.
str = input("enter a string:")

count = 0

for ch in str:
    if ch in "aeiouAEIOU":
        count += 1
print("number of vowles presnet in a string is:", count)        