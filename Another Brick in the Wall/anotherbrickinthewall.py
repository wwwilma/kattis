# A program to thell whether the construction worker will complete the wall with the new pile of bricks

# Defining the testing function that takes bricks, height, and width as paramters
def brick_test(bricks, height, width):
    leftHeight = height
    leftWidth = width
    index = 0  # initialize index variable to 0
    while 0 < leftHeight:  # looping the height and width 
        while 0 < leftWidth:
            brick = bricks[index]
            if brick <= leftWidth:
                leftWidth -= brick
                index += 1  # incrementing the index variable
            else:
                return False

        leftHeight -= 1
        leftWidth = width
    return True


height, width, bricksAmount = list(map(int, input().split()))
bricks = list(map(int, input().split()))
possible = brick_test(bricks, height, width)

if possible:  # finally, printing whether it is possible for the construction worker or not
    print("YES")
else:
    print("NO")