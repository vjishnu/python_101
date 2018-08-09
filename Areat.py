
a = int(input("Enter the base"))
b= int(input("Enter the height"))

area = (a*b)/2

print("Area of the Triangle is ",area)

# area with 3 sides with import math
import math
a = int(input("Enter the first"))
b= int(input("Enter the height"))
c= int(input("Enter the height"))

s = (a+b+c)/2

l = (s*(s-a)*(s-b)*(s-c))
print("Area of the Triangle is ",math.sqrt(l))



