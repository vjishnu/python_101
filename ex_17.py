the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")



# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")


# also we can go through a mixed list too
# notice we have to use {} since we dont know what is in it

for i in change:
    print("I got", {i})

# we can also build list, first start with an empty one

elements = []

#then use the range function to do the 0 to 5 counts

for i in range(0,6):
    print("Adding " ,{i} ,"to the list.")
    #append is a function that lists understand
    elements.append(i)

# to list out the items in elements
for i in elements:
    print("The element is " , {i})



