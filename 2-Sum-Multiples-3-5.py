def sum_multiples(threshold, *args):
    """
    Takes a threshold of numbers to go below. For example, 10
      Then it will sum the numbers that are multiples of *args
      you pass.
    :param threshold: integer
    :param *args: integer (multiples you want to pass) 3, 5
    """
    sum = 0
    summed_multiples = []
    for x in range(1, threshold, 1):
        for a in args:
            if (x%a) == 0 and x not in summed_multiples:
                sum += x
                summed_multiples.append(x)
    return sum

def main():
    print(sum_multiples(10,3,5))  # returns 23
    print(sum_multiples(1000,3,5))  # returns 233168


if __name__ == "__main__":
    main()
