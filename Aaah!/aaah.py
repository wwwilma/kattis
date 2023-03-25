# Prompt the user to enter two strings and store 
# them in buffer1 and buffer2 variables.
buffer1 = input("Enter string 1: ")
buffer2 = input("Enter string 2: ")

# Use a ternary operator to print "no" if buffer1 is shorter than buffer2, 
# otherwise print "go".
# The len() function is used to get the length of each buffer.
if len(buffer1) < len(buffer2):
    print("no")
else:
    print("go")