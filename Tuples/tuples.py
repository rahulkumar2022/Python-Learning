
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[0])
print(thistuple[1:3])
print(thistuple[-2])    

# Tuples are immutable, so we cannot modify them like lists
# thistuple[1] = "orange"  # This will raise a TypeError

# updating tuples
y = list(thistuple)  # Convert to list
y[1] = "orange"  # Modify the list
thistuple = tuple(y)  # Convert back to tuple
print(thistuple)
