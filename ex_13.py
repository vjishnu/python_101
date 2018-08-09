import sys

print('Arguments:', len(sys.argv))# to find the total no of arguments
print('List:', str(sys.argv)) # to display the list of arguments

filename = sys.argv[1:]
print('Filename:', filename)
