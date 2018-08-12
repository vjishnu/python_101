                      # ....vowels in a String....
"""Read a string from user and count the number of vowels in the given String"""        
print("...vowels in a string....")
my_string = input("Enter the string : ")
vowels = "aeiou"
count = 0

for i in my_string:
    for j in vowels:
        if i==j:
            count+=1
print(f"The number of vowels in the given string is {count}.")

'''input  :
              ...vowels in a string....

        Enter the string : i like apple
   output :
        The number of vowels in the given String is 5.'''
print(".........................")

                    # ....Reverse of a string....
   
"""Read a string from user and reverse and print the string."""
print("...Reverse of a string....")
string = input("Enter the string : ")
reverse = string[::-1]
print("The string is{} ".format(string))
print("The reversed string is  {} ".format(reverse))

"""input  :
                  ...Reverse of a string...

             Enter the string : i love python
    output :
             The reversed string is nohtyp evol i """
print("............................")

                     # ....Palindrome String....

"""Read a string from user and check whether it is palindrome or not"""
print("....palindrome sequence....")
string  = input("Enter the string")
rev = string[::-1]

if string==rev:
    print("The enterted string is palindrome")
else:
     print("The entered string is not palindrome")
print("............................")


                        # BMI calculator

"""Read height and weight from user and calculate the Body Mass Index of the user."""
print("....BMI CALCULATOR....")
height = float(input("Input your height in meters: "))
weight = float(input("Input your weight in kilogram: "))
bmi =  (weight / (height * height))
print(f"Your body mass index is {bmi}.")
print("..................")

'''Input :
             ....BMI calculator....
             Input your height in meters: 1.8
             Input your weight in kilogram: 60
      Output: 
             Your body mass index is 18.51851851851852.
           .................. '''

                    # Factorial of a Number
"""Read a number from user and find its factorial."""
print("....Factorial of a number....")
num = int(input("Enter the number"))
product = 1
for i in range(num):
    product = product * (i+1) # 4! = 4*3*2*1
print(f"The factorial of the given number is {product}.")
print(".......................")

'''input :
                 ....Factorial of a number....

                Enter the number7
      output :
                The factorial of the given number is 5040.

                 .......................'''

     # using math

import math
from math import factorial
print("....Factorial of a number using buildin function....")
num = int(input("Enter the number"))
fact = math.factorial(num)
print(f"The factorial of the given number is {fact}.")
print(".......................")


                   #  Print * in a Traingle pattern
'''Read no of rows from user and print a triangle pattern using * character'''
print("....Print * in a Traingle pattern....")
num = int(input("Enter the numbr of rows : "))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
  
'''input :
             Enter the numbr of rows : 5
       output :
    *
   * *
  * * *
 * * * *
* * * * *  
..................'''

                  # sort a string in alphabetical order
'''read a string and sort it in alphabetical order.'''
print("....sort a string in alphabetical order....")
s1=input("Enter the string to sort in alphabetic order :")
b =''.join(sorted(s1)) # remove space between them using join function.
print(b)
print("...........................")

'''input  :
             Enter the string to sort in alphabetic order : i love python
       output : ehilnooptvy
...........................'''


              # remove punctuations from the given string

''' Read a string from user with punctuations and remove all the punctuations and print it.'''
print("....Removing punctuations from the String....")
print("Press 'x' for exit :")
string = input("Enter any string to remove all punctuations of it : \n")

if string == 'x':#if user entered 'x' , then it will exit.
    exit()
else:
    newstr = string # assign the string to newstr
    print("\n Remove all punctuations from the string...\n")
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' # common punctuations in a string
    for x in string.lower():
        if x in punctuations:
            newstr = newstr.replace(x,"")
print(f"New string after removing all punctuations is \n : \n {newstr}.")
print(".........................")

'''input  :
             ....Removing punctuations from the String....
                 Press 'x' for exit :
                 Enter any string to remove all punctuations of it :
                 
                 hshfiuhdiogihhjh^&^^%^$$#Hhvgh&*^&^%$#>>......"";

                 Remove all punctuations from the string...

                 New string after removing all punctuations is
      output : 
                 hshfiuhdiogihhjhHhvgh.
                ......................... '''
