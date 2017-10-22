"""
This program creates a list of numbers from a file,
sqares each number,
and takes the sum of the squares.
"""

# Iterate over the length of the list and square each element of the list.
def square(numlist):
    for i in range(len(numlist)):
        # Exclude empty strings.
        if numlist[i] != "":
            x = eval(numlist[i])
            square = x*x
            numlist[i] = square
            print(numlist)
        else:
            i = i + 1

# Take the sum of all elements in th elist.
def sumElemts(numlist):
    sum_nums = 0
    for i in numlist:
        if i != "":
            sum_nums = sum_nums + i
        else:
            return sum_nums

def main():
    # Prompt the user for a file to open and read the file.
    filename = open(input("please enter a file name: "), "r")
    numFile = filename.read()

    # Create an empty list.
    numlist = numFile.split("\n")
    squared_nums = square(numlist)
    print(sumElemts(numlist))
main()
