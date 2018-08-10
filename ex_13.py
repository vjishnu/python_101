import sys

print('Arguments:', len(sys.argv))# to find the total no of arguments
print('List:', str(sys.argv)) # to display the list of arguments

filename = sys.argv[1:]
print('Filename:', filename)

count=len(sys.argv)
if count > 0:
    print("there are {} arguments".format(count))
else:
    print("There are no arguments")
