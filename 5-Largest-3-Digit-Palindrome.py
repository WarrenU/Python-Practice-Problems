def is_palindrome(int_result):
    """
    Casts an int result to a string, and reverses it.
    We check to see if the int result is the same written backwards.
    """
    return str(int_result) == str(int_result)[::-1]

def find_palindrome():
    """
    Finds the largest palindromic number for the product
     of two 3 digit integers (100-999).
    If you run the code you have the answer ;)
    """
    largest_palindrome = 0
    y=999
    for x in range(100,1001):
        for y in range(100, 1001):
            result = x*y
            if result > largest_palindrome and is_palindrome(result):
                largest_palindrome = result
    return largest_palindrome

def main():
    print(find_palindrome())


if __name__ == "__main__":
    main()
