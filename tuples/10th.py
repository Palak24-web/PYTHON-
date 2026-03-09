# Remove duplicate elements from a tuple.

t = (10,23,34,45,10)

t_unique = tuple(set(t))

print("tuple without duplicates:",t_unique)