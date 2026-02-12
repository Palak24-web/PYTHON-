# Write a program to find the longest word in a sentence.

a = input("enter a sentence")

words = a.split() # breaks the sentence into words
longest = "" # stores the longest word found so far

for word in words:
    if len(word)>=len(longest):
        longest =  word

print("longest word is:",longest)        
        