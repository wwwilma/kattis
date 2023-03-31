# Import the necessary module
import sys

# Read the input line with integers, convert to list, and sort in ascending order.
nums = [int(x) for x in sys.stdin.readline().strip().split()]
nums.sort()

# Create a dictionary to pair up the sorted integers with letters A, B, C.
pairup = {}
for i in range(3):
    pairup[chr(ord('A') + i)] = nums[i]

# Read the input line with characters and iterate over each character.
message = sys.stdin.readline().strip()
for c in message:
    # Output the corresponding integer from the dictionary for each character.
    # If the character is not in the dictionary, the code will raise a KeyError.
    print(pairup[c], end=' ')