import unittest
from solution import solution as original_solution


class TestMultiplyArrays:
    def test_given_example(self):
        arr1 = [1, 9, 3, 7, 0, 7, 7, 2, 1]
        arr2 = [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7]
        result = self.func(arr1, arr2)
        self.assertEqual(
            result, [-1, 4, 7, 5, 7, 3, 9, 5, 2, 5, 8, 9, 6, 7, 6, 4, 1, 2, 9, 2, 7]
        )


class TestSolution(TestMultiplyArrays, unittest.TestCase):
    def setUp(self):
        self.func = original_solution


if __name__ == "__main__":
    unittest.main()
