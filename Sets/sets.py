thisset = {"apple", "banana", "cherry","Mango"}
print(thisset)
thisset.add("orange")
print(thisset)
thisset.add("apple")
print(thisset)

myset = {"apple", "banana", "cherry",True, 0,1, False}
print(myset)

for x in myset:
    print(x)

if("banana" in myset):
    print("Yes, 'banana' is in the set")
else:
    print("No, 'banana' is not in the set")

myset.update(thisset);
print(myset)

#adding elements from a list
myList = ["apple", "banana", "cherry",1,2,3,4];
myset.update(myList);
print(myset)

myset.remove("banana")
print(myset)

#remove random element
x = myset.pop()
y = myset.pop()
print(f"Removed elements: {x}, {y}")
print(myset)

myset.clear()
print(myset)

del myset
# print(myset)  # This will raise a NameError since myset is deleted    

set1 = {"a","b", "c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)

set4 = set1 | set2  # Another way to union sets
print(set4)

set5 = {"d","e","true",0,1}

set6 = set1|set2|set5  # Union of multiple sets
print(set6)

set2.update(set1)
print(set2)

set7 = set2.intersection(set5)  # Intersection of sets
print(set7)

set8 = set2 & set5  # Another way to find intersection
print(set8)