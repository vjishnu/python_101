import sys 
prgrm_name = sys.argv[0]


arguments = sys.argv[1:]
count = len(arguments)

from sys import argv
script,first,second,third=argv
print(" Total no of arguments in command line is : ",count)
print("The script is called : " ,script)
print("The first variable is called : " ,first)
print("The second variable is called : " ,second)
print("The thrid variable is called : " ,third)
if arguments > 0:
    count = len(arguments)
    print("The no. of arguments is {}".format(count))
elif arguments < 0:
     print("There are no arguments")
    

