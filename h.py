a=int(input("Enter the 1st no."))
b=int(input("Enter the 2st no."))
c=int(input("Enter the 3st no."))

if (a>b) and (a>c):
    largest = a
elif (b>c) and (b>a):
     largest = b
else: 
     largest = c
print("The largest of given number is {}".format(largest)) 
     

