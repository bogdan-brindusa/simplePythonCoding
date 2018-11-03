# Using some functions from 'math' module

import math

# function that prints square root of a and b
def square_root(x, y):
  print('Square root of %d is: %.2f' %(x, math.sqrt(x)))
  print('Square root of %d is: %.2f' %(y, math.sqrt(y)))

# function that prints result of a to the power of b
def power(x, y):
  print('%d to the power of %d is: %d' %(x, y, math.pow(x, y)))

# function that prints length of the vector from origin (0, 0) to point (a, b)
def vector(x, y):
  print('Vector length from origin(0, 0) to point (%d, %d) is: %.2f' %(x, y, math.hypot(x, y)))

# working with two numeric variables
a = int(input('Give a value for a: '))
b = int(input('Give a value for b: '))

# calling functions
square_root(a, b)
power(a, b)
vector(a, b)
