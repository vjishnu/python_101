from sys import argv
from os.path import exists # tocheck whether the file is exists or not
script , from_file , to_file = argv

print(f"copying from {from_file} to {to_file}")

in_file = open(from_file) # open the file and assign into a variable in_file
indata = in_file.read() # copy the data inside the file to another variable indata

print(f"The input file is {len(indata)} bytes long") 

print(f"Does the output file exists? {exists(to_file)}") #checks the file exists or not
print(f"Ready hit RETURN to continue, CRTL-c to abort.")
input()

out_file = open(to_file,'a') # open an existing file or a new file that we want to write or append the data from the from_file 
out_file.write(indata) # write the contents of data from indata variable to another variable out_file

print(f"alright, all done.")

out_file.close() # close out_file
in_file.close() # close in_file
