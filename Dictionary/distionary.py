thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "electric": False,
    "colors": ["red", "white", "blue"]
}

print(thisdict)

print(thisdict["brand"])
print(thisdict["model"])
print(thisdict["year"])
# print(thisdict["test"]) # KeyError: 'test' because 'test' is not a key in thisdict

dictonary = dict(name="John", age=30, city="New York")
print(dictonary)

dictonary["age"] = 31  # Update the value of the key "age"
print(dictonary)

dictonary["country"] = "USA"  # Add a new key-value pair
print(dictonary)

dictonary.pop("city")  # Remove the key "city"
print(dictonary)

for x in dictonary:
    print(x)  # Print the keys

for x in dictonary.keys():
    print(dictonary[x])  # Print the values
    print("x:", x, "value:", dictonary[x])  # Print keys and their corresponding values

for x, y in dictonary.items():
    print("key:", x, "value:", y)  # Print keys and their corresponding values