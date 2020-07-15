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
import math


def iterative_printer(nums: list) -> None:
    """
    Takes a list of integers and prints them out so that the first line shows
      the first element, the next line shows the next two elements,
      the third line shows the next three elements and so on.
    :param nums: list
    """
    lbound = 0
    rbound = 1
    limit = math.ceil(len(nums)/2)
    for i in range(limit):
        vals = [str(e) for e in nums[lbound:rbound]]
        print(" ".join(vals))
        lbound = rbound
        rbound = rbound + i+2
    print()

def main():
    l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    iterative_printer([2,1,3,0,4,7])
    iterative_printer([2,1,3,0,4,7,5,8])
    iterative_printer(l)


if __name__ == "__main__":
    main()
