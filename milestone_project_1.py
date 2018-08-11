# ....vowels in a String....
print("...vowels in a string....")
"""Read a string from user and count the number of vowels in the given String"""
"""input : 
Enter the string : i like apple
output :
The number of vowels in the given String is 5."""
my_string = input("Enter the string : ")
vowels = "aeiou"
count = 0

for i in my_string:
    for j in vowels:
        if i==j:
            count+=1
print(f"The number of vowels in the given string is {count}.")
# ....Reverse of a string....
print("...Reverse of a string....")
"""Read a string from user and reverse and print the string."""
"""input:
Enter the string : i love python
output :
The reversed string is nohtyp evol i """

string = input("Enter the string : ")
reverse = string[::-1]
print("The string is{} ".format(string))
print("The reversed string is  {} ".format(reverse))

# ....Palindrome String....
print("....palindrome sequence....")

"""read a string from user and check whether it is palindrome or not"""
string  = input("Enter the string")
rev = string[::-1]

if string==rev:
    print("The enterted string is palindrome")
else:
     print("The entered string is not palindrome")
     print("............................")


# BMI calculator
print("....BMI CALCULATOR....")
"""read height and weight from user and calculate the Body Mass Index of the user."""
print("....BMI calculator....")
height = float(input("Input your height in meters: "))
weight = float(input("Input your weight in kilogram: "))
bmi =  (weight / (height * height))
print(f"Your body mass index is {bmi}.")
print("..................")


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

