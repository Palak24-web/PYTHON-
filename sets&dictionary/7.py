# o={} # empty dictionary
s={1,2,5,6,"okay"} # set with values

e=set() # empty set , don't use e={} as it will create empty dictionary

print(s) # in set elements are not repeated and order is not maintained

s.add(578)
print(s)

s.discard(2)   # removes 2 from the set if present and shifts it to the last position otherwise does nothing

s.remove(5)
print(s)
