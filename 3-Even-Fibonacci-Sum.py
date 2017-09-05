
def even_fib(threshold):
    """
    Sums fibonacci numbers that are even below the threshold number.
    :param threshold: int (threshold)
    """
    p, n = 0, 1
    fsum = 0
    while(n < threshold):
        fib_num = p + n
        p = n
        n = fib_num
        # print(fib_num)
        if(fib_num % 2 == 0):
            fsum += fib_num
    return fsum


def main():
    print('\nEven Fib Sum: {}'.format(even_fib(4000000)))

if __name__ == "__main__":
    main()
