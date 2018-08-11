# ....Palindrome String....
"""read a string from user and check whether it is palindrome or not"""
string  = input("Enter the string")
rev = string[::-1]

if string==rev:
    print("The enterted string is palindrome")
else:
     print("The entered string is not palindrome")
     print("..............")
