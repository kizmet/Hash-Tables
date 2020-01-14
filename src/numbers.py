# Add up and print the sum of all of the minimum elements of each inner array:
# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# Understand
# minimum = lowest
# find the lowest within each array
# sum total of all the numbers found

# Plan
# loop through numberslist
# smallestInList
# within each list in numberslist
# if number i is smaller than smallestInList
# add smallestInList to a new numberslist called minnumberlist

# to sum
# set variable sum
# loop through each number in minnumberlist
# add number to sum

numberslist = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]


def smallestInnner(numberslist):
    minnumbers = []
    for numbers in numberslist:
        smallestnumber = numbers[0]
        for number in numbers:
            if number < smallestnumber:
                smallestnumber = number
                # print(smallestnumber)
        minnumbers.append(smallestnumber)
    return minnumbers


def addminnums(minnumbers):
    numsum = 0
    for number in minnumbers:
        numsum = numsum + number
    return numsum


x = smallestInnner(numberslist)
y = addminnums(x)
print(y)
