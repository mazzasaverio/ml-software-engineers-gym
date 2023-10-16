import unittest
from solution import solution as original_solution


class TestMultiplyArrays(unittest.TestCase):
    def setUp(self):
        self.func = original_solution

    def test_given_example(self):
        arr1 = [1, 9, 3, 7, 0, 7, 7, 2, 1]
        arr2 = [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7]
        result = self.func(arr1, arr2)
        self.assertEqual(
            result, [-1, 4, 7, 5, 7, 3, 9, 5, 2, 5, 8, 9, 6, 7, 6, 4, 1, 2, 9, 2, 7]
        )

    def test_both_positive(self):
        arr1 = [1, 2, 3]
        arr2 = [4, 5, 6]
        result = self.func(arr1, arr2)
        self.assertEqual(result, [5, 6, 0, 8, 8])

    def test_both_negative(self):
        arr1 = [-1, 2, 3]
        arr2 = [-4, 5, 6]
        result = self.func(arr1, arr2)
        self.assertEqual(result, [5, 6, 0, 8, 8])

    def test_one_negative(self):
        arr1 = [-1, 2, 3]
        arr2 = [4, 5, 6]
        result = self.func(arr1, arr2)
        self.assertEqual(result, [-5, 6, 0, 8, 8])

    def test_with_zeros(self):
        arr1 = [0]
        arr2 = [1, 2, 3]
        result = self.func(arr1, arr2)
        self.assertEqual(result, [0])

    def test_single_digit_numbers(self):
        arr1 = [5]
        arr2 = [6]
        result = self.func(arr1, arr2)
        self.assertEqual(result, [3, 0])

    def test_one_single_one_multi(self):
        arr1 = [5]
        arr2 = [1, 2, 3]
        result = self.func(arr1, arr2)
        self.assertEqual(result, [6, 1, 5])


if __name__ == "__main__":
    unittest.main()
