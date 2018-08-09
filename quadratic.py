from  math import sqrt #import sqrt function from math

a = int(input("Enter the 1st coifficient")) # read from user
b = int(input("Enter the 2st coifficient")) # read from user
c = int(input("Enter the 3st coifficient")) # read from user


disc = b**2 - 4*a*c # to find the discriminent
disc1 = sqrt(disc)# thn find the square root of discriminent
# in a quadratic equation there are postive and negative solution
post = (-b+disc1) /(2*a) # postive solution
neg = (-b-disc1) / (2*a) # negative solution

print("The postive solution is {} and the negative solution {}".format(post,neg))




