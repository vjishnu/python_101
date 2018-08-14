stack=['dog','cat','parrot'] # list as stack
# before appending
print(stack)
#entering item to append
item=str(input("Enter the item to append"))
#after appending to the stack
print("The item appended is {0}".format(item))
print(stack.append(item))
print(stack)
