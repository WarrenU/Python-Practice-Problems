# Question:
# We have a list of integers.
# Write a function that prints the contents of the array so that the first line shows the first element,
# the second line shows the next two elements,
# the third line shows the next three elements and so on.

# Example input:1) [2,1,3,0,4,7]
#               2) [2,1,3,0,4,7,5,8]
#
# Example output: 1) Output:2
#                           1 3
#                           0 4 7
#                 2) Output:2
#                           1 3
#                           0 4 7
#                           5 8

# Explanation to my answer:
#
# My approach is using a left bounded and right(upper) bounded number.
#  upon every iteration it will lastly set the left bound where the upper right
#  bound had left off.
#
#  And to calculate the right bound I added up the numbers it was on per iteartion.
#    For example: The first iteartion would need a rbound of 1
#                 The second iteration would need a rbound of 3 (1 + 2)
#                 The third iteration would need a rbound of 6 (1 + 2 + 3)
#                 The fourth iteration would need a rbound of 10 (1+ 2 + 3 + 4)
#                 ..etc


def iterative_printer(l):
    """
    Takes a list of integers and prints them out so that the first line shows
      the first element, the next line shows the next two elements,
      the third line shows the next three elements and so on.
    :param l: list
    """
    lbound = 0
    rbound = 1
    for i in range(len(l)):
        rbound = 0
        # Need to add 1 to account for 0 based indexes.
        for x in range(i+1):
            rbound += x+1 #  This is where (1+2+3) etc math occurs.
        print(' '.join(map(str, l[lbound:rbound])))
        if rbound >= len(l):
            break  # if we have reached the last element or beyond, we are done.
        lbound = rbound
    print('\n')


def main():
    l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    iterative_printer([2,1,3,0,4,7])
    iterative_printer([2,1,3,0,4,7,5,8])
    iterative_printer(l)


if __name__ == "__main__":
    main()
