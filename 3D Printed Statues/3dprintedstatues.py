# Read an integer from the user and store it in n.
# This represents the number of statues you need to print.
n = int(input())

# Initialize a variable i to 0, 
# which will be used to count the number of bits required to represent n in binary.
i = 0

# Keep shifting the binary representation of 2 to the left, 
# until it is greater than or equal to n.
while 2**i < n:
    i += 1

# Add 1 to i and print it, 
# since the number of bits required to represent n is equal to i plus 1.
# I.e. this is the minimum number of days to print the required statues.
print(i + 1)