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
print(f"The number of vowels in the given String is {count}.")	      
	      
