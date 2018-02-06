# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# TODO: Add Docstrings and explanations.
def gcd(x,y):
    while y != 0:
        x, y = y, x % y
    return x

def lcm(x,y):
    return x*y//gcd(x,y)

def lcmCalculation(first_r_val, *args):
    for v in args:
        first_r_val = lcm(first_r_val, v)
    return first_r_val

def main():
    print(lcmCalculation(*range(1,11)))
    print(lcmCalculation(*range(1,21)))


if __name__ == "__main__":
    main()