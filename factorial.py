# Factorial of a Number
"""Read a number from user and find its factorial."""
print("....Factorial of a number....")
num = int(input("Enter the number"))
product = 1
for i in range(num):
    product = product * (i+1) # 4! = 4*3*2*1
print(f"The factorial of the given number is {product}.")
'''input :
Enter the number7
output :
The factorial of the given number is 5040.'''

print(".......................")

# using math 

import math
from math import factorial
print("....Factorial of a number using buildin function....")
num = int(input("Enter the number"))
fact = math.factorial(num)
print(f"The factorial of the given number is {fact}.")

print(".......................")


