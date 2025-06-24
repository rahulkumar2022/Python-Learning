def my_function():
    print("This is my function.")


my_function()

#function with parameters
def my_function(fname, lname):
    print("My name is " + fname + " " + lname)

my_function("John", "Doe")

# If number of arguments in the function is unknown
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")