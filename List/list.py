myList = ["1","8","2", "3", "4", "5"]
print(myList)
myList.append("6")
print(myList)
myList.insert(0, "0")
print(myList)
myList.remove("3")
print(myList)
print(len(myList))
myList.pop()
print(myList)
myList.sort()
print(myList)
myList.reverse()
print(myList)

print(myList[0])
print(myList[1:3])
print(myList[-2])

myList2 = myList.copy()
myList2.reverse()
print(myList2)
myList2[1] = "99"
print(myList2)
print(myList2.count("99"))
myList2[1:3]= ["88", "77"]
print(myList2)
myList2.insert(2, "66")
print(myList2)
myList2.extend(["11", "22"])
print(myList2)
myList2.append("33")
print(myList2)
myList2.extend(myList)
print(myList2)
myList2.pop();
myList2.pop(0)
print(myList2)
del myList2[0]
print(myList2)
# myList2.clear()
# print(myList2)

# loop through list
for item in myList2:
    print(item)

# loop through list with index
for i in range(len(myList2)):
    print(f"Index {i}: {myList2[i]}")

# using while loop
i = 0
while i < len(myList2):
    print(f"While Index {i}: {myList2[i]}")
    i += 1

# List comprehension
[print(x) for x in myList2]


newList = []
for x in myList2:
    if x.isdigit() and int(x) % 2 == 0:
        newList.append(x)
print(newList)

# List comprehension for even numbers
evenList = [x for x in myList2 if x.isdigit() and int(x) % 2 == 0]
print(evenList)

# sorting with a list
evenList.sort();
print(evenList)
evenList.sort(reverse=True)
print(evenList)

def myFunction(x):
    return int(x) % 4 == 0

evenList.sort(key=myFunction)
print(evenList)

newList = myList + myList2
print(newList)

