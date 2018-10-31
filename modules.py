# Using some functions from 'math' module

import math

# working with two numeric variables
a = int(input('Give a value for a: '))
b = int(input('Give a value for b: '))

# print square root of a and b
print('Square root of %d is: %.2f' %(a, math.sqrt(a)))
print('Square root of %d is: %.2f' %(b, math.sqrt(b)))

# print result of a to the power of b
print('%d to the power of %d is: %d' %(a, b, math.pow(a, b)))

# print length of the vector from origin (0, 0) to point (a, b)
print('Vector length from origin(0, 0) to point (%d, %d) is: %.2f' %(a, b, math.hypot(a, b)))
