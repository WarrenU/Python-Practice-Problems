def determineLargestPrimeFactor(lpf_value):
    """
    Returns the largest prime factor value, that is a prime factor of x.
    int x: Integer to find largest prime factor of.
    return int lpf: Largest prime factor integer.
    """
    possible_lpf = 2
    while(possible_lpf * possible_lpf < lpf_value):
        while(lpf_value % possible_lpf == 0):
            lpf_value /= possible_lpf
        possible_lpf += 1
    return lpf_value


def main():
    print(determineLargestPrimeFactor(600851475143))


if __name__ == "__main__":
    main()
