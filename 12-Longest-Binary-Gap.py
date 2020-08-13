import unittest

# the largest integer we have to deal with
MAXINT = 2147483647

def validate(num: int):
    """
    determines if the input is valid
    """
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    if num < 1 or num > MAXINT:
        raise ValueError("Input must be between 1 and 2147483647")

def get_max_gap(num: int) -> int:
    """
    Determines the maximal 'binary gap' of an integer converted to binary rep.
        :param num: a positive integer (between 1 and 2,147,483)
        :return: Count of longest sequence of 0's in the binary representation  of a number.
    """
    validate(num)
    binary_string = str(bin(num))[2:]
    answer = 0
    count = 0
    for bit in binary_string:
        if bit == "0":
            count += 1
        if bit == "1":
            if count > answer:
                answer = count
            count = 0
    return answer

class TestBinaryGap(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(5, get_max_gap(1041))

    def test_example2(self):
        self.assertEqual(0, get_max_gap(15))

    def test_extremes(self):
        self.assertEqual(0, get_max_gap(1))
        self.assertEqual(1, get_max_gap(5))
        self.assertEqual(0, get_max_gap(MAXINT))

    def test_trailing_zeros(self):
        self.assertEqual(get_max_gap(6), 0)
        self.assertEqual(get_max_gap(328), 2)

    def test_simple1(self):
        self.assertEqual(get_max_gap(9), 2)
        self.assertEqual(get_max_gap(11), 1)

    def test_simple2(self):
        self.assertEqual(get_max_gap(19), 2)
        self.assertEqual(get_max_gap(42), 1)

    def test_simple3(self):
        self.assertEqual(get_max_gap(1162), 3)
        self.assertEqual(get_max_gap(5), 1)

    def test_medium1(self):
        self.assertEqual(get_max_gap(51712), 2)
        self.assertEqual(get_max_gap(20), 1)

    def test_medium2(self):
        self.assertEqual(get_max_gap(561892), 3)
        self.assertEqual(get_max_gap(9), 2)

    def test_medium3(self):
        self.assertEqual(get_max_gap(66561), 9)

    def test_large1(self):
        self.assertEqual(get_max_gap(6291457), 20)

    def test_large2(self):
        self.assertEqual(get_max_gap(74901729), 4)

    def test_large3(self):
        self.assertEqual(get_max_gap(805306369), 27)

    def test_large4(self):
        self.assertEqual(get_max_gap(1376796946), 5)

    def test_large5(self):
        self.assertEqual(get_max_gap(1073741825), 29)

    def test_large6(self):
        self.assertEqual(get_max_gap(1610612737), 28)

    def test_validations(self):
        self.assertRaises(TypeError, get_max_gap, 1.0)
        self.assertRaises(ValueError, get_max_gap, 0)
        self.assertRaises(ValueError, get_max_gap, 2147483648)


if __name__ == '__main__':
    unittest.main()
