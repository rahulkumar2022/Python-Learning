
a = 33
b = 200

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:   
    print("a is greater than b")


if a > b: print("a is less than b") 

print("a is less than b") if a < b else print("a is greater than or equal to b")

a = 200
b = 33
c = 500

if a>b and c> a:
    print("Both conditions are True")
if a > b or a > c:
    print("At least one of the conditions is True")

if not (a < b):
    print("a is not greater than b")