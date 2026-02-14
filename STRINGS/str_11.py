#  Find the frequency of each character in a string.

str = input("enter a string=")

freq ={}  

for ch in str:
    if ch in freq: 
        freq[ch]=freq[ch]+1 
    else:
        freq[ch]=1

print(freq)     

