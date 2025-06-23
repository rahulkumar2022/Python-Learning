print(10>9)
print(10 == 9)
print(10 < 9)
print(10 != 9)

a = 10
b = 20

if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")


print(bool("Hello"))
print(bool(15))  # True
print(bool(""))  # False
print(bool(0))  # False
print(bool(None))  # False
print(bool(()))  # False
print(bool([]))  # False
print(bool({}))  # False    
print(bool({"name": "John"}))  # True


class myClass():
    def __len__(self):
        return 0
    
myObj = myClass()
print(bool(myObj))  # False, because __len__ returns 0


# Check if object of integer or not
x = 200
print(isinstance(x, int))  # True
print(isinstance(x, float))  # False