x = 1
y = 2.8
z = 1j

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>

x = 35e3
y = 12E4
z = 87.7e100

print(type(x))  # <class 'float'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'float'>

x = 3+5j
y = 5j
z = -5j

print(type(x))  # <class 'complex'>
print(type(y))  # <class 'complex'> 
print(type(z))  # <class 'complex'>

# Type conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

a = float(x)  # convert from int to float
print(a)  # 1.0
print(type(a))  # <class 'float'>

b = int(y)  # convert from float to int
print(b)  # 2
print(type(b))  # <class 'int'>

# c = int(z)  # convert from complex to int
# print(c)  # Raises ValueError: can't convert complex to int
d = complex(x)  # convert from int to complex
print(d)  # (1+0j)
print(type(d))  # <class 'complex'>


import random
print(random.randrange(1, 10))  # Returns a random integer from 1 to 9

# print(random.randint(501,500))  # Returns a error because the first argument is greater than the second