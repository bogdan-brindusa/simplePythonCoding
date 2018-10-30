# User is asked to give values for 2 numbers
x = int(input("Give an integer value to x: "))
y = int(input("Give an integer value to y: "))

# Calculate and print sum
summ = x + y
print("x + y = %d" %summ)

# Calculate and print division
div = x / y
print("x / y = %.2f" %div)

# Calculate and print exponent
exp = x ** y
print("x to the power of y = %d" %exp)

# Concatenating two strings
fname = input("First name: ")
lname = input("Surname: ")
fullName = fname + " " + lname
print("Your name is %s" %fullName)
