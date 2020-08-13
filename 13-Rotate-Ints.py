import unittest
import random

ARRAY_RANGE = (-1000, 1000)
INT_RANGE = (0, 100)


def rotate_by(l: list, rots: int) -> list:
    """
    Rotate the array `l` by x amount of rotations `rots`
        :param l: an array of integers
        :param rots: number of times to shift right
        :return: the rotated array
    """
    last_elems = l[-rots:]
    beginning_elems = l[:-rots]
    last_elems += beginning_elems
    return last_elems


class TestCyclicRotation(unittest.TestCase):

    def test_no_rotations(self):
        self.assertEqual(rotate_by([6, 3, 8, 9, 7], 0), [6, 3, 8, 9, 7])

    def test_one_rotation(self):
        self.assertEqual(rotate_by([6, 3, 8, 9, 7], 1), [7, 6, 3, 8, 9])

    def test_three_rotations(self):
        self.assertEqual(rotate_by([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])

    def test_full_rotation(self):
        self.assertEqual(rotate_by([6, 3, 8, 9, 7], 5), [6, 3, 8, 9, 7])

    def test_empty_list(self):
        self.assertEqual(rotate_by([], 5), [])

    def test_random(self):
        N = random.randint(*INT_RANGE)
        K = random.randint(*INT_RANGE)
        A = [random.randint(*ARRAY_RANGE) for i in range(0, N)]
        print(N, K, A)
        print(rotate_by(A, K))

if __name__ == '__main__':
    unittest.main()