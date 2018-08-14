def add(a,b):
    return a+b
a = int(input("Enter 1st  number : "))
b = int(input("Enter 2nd number "))
print("The sum is : ",add(a,b))

def cheese_and_crackers(cheese_count,box_of_cheeses):
    return cheese_count , box_of_cheeses
cheese_count = int(input("Enter the no. of cheese count")) 
box_of_cheeses = int(input("Enter the no. of boxes of cheess"))
cheese_and_crackers(cheese_count,box_of_cheeses)
print(f"You have {cheese_count} cheeses!")  
print(f"You have {box_of_cheeses} boxes of crackers!") 
