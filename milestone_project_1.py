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

