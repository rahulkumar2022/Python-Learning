# name = input("Enter your name: ")

# name = name.strip()

# print(f"Hello world!, {name}")

# slicing the string
b = "Hello world!"
# upper limit is exclusive, lower limit is inclusive
# b[0:5] means from index 0 to index 5 (exclusive)
# b[6:11] means from index 6 to index 11 (exclusive)
# b[2:5] means from index 2 to index 5 (exclusive)
print(b[0:5])  # Hello
print(b[6:11])  # world
print(b[2:5])  
print(b[:5]) 
print(b[2:])

print(b.upper())  # HELLO WORLD!
print(b.lower())  # hello world!

b = " Hello World! "
print(b.strip())  # 'Hello World!' removes any whitespace from the beginning and the end
print(b.lstrip())  # 'Hello World! ' removes any whitespace from the beginning
print(b.rstrip())  # ' Hello World!' removes any whitespace from the end


print(b.replace("H", "J"))  # Jello World! replaces H with J
print(b.replace("o","e"))

print(b.split(" "))  # ['Hello', 'World!'] splits the string into a list where each word is a list item
b = " Hello, World!, Python "
print(b.split(","))  # [' Hello',' World!',' python'] splits the string into a list where

a = "Hello"
b = "World"
c = a + " " + b  # Concatenation of strings
print(c)  # Hello World
c = a+b
print(c)  # HelloWorld


# Format strings
age = 36
#txt = "My name is John, and I am " + age # Raises TypeError: can only concatenate str (not "int") to str
txt = "My name is John, and I am " + str(age)
print(txt)  # My name is John, and I am 36
txt = "My name is John, and I am {}".format(age)
print(txt)  # My name is John, and I am 36
txt = f"My name is John, and I am {age}"
print(txt)  # My name is John, and I am 36


price = 49
txt = f"The price is {price} dollars"
print(txt)  # The price is 49 dollars
txt = f"The price is $ {float(price)}"
print(txt)  # The price is $ 49.0
txt = f"The price is {price:.2f} dollars"
print(txt)  # The price is 49.00 dollars

print(f"The price is {10*10} dollars")  # The price is 100 dollars