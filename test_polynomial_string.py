import unittest
from polynomialString import get_polynomial_string


class MyTestCase(unittest.TestCase):
    def test_working(self):
        ret = get_polynomial_string([8, 2, 4, 6])
        self.assertEqual(ret, "8(x^3) + 2(x^2) + 4x + 6")

    def test_empty_list(self):
        ret = get_polynomial_string([])
        self.assertEqual(ret, "0")

    def test_zero(self):
        ret = get_polynomial_string([0])
        self.assertEqual(ret, "0")

    def test_zeros(self):
        ret = get_polynomial_string([0, 0])
        self.assertEqual(ret, "0")

    def test_leading_zero(self):
        ret = get_polynomial_string([0, 2, 4, 6])
        self.assertEqual(ret, "2(x^2) + 4x + 6")

    def test_leading_zeros(self):
        ret = get_polynomial_string([0, 0, 4, 6])
        self.assertEqual(ret, "4x + 6")

    def test_zeros_middle(self):
        ret = get_polynomial_string([2, 0, 0, 6])
        self.assertEqual(ret, "2(x^3) + 6")

    def test_zero_middle(self):
        ret = get_polynomial_string([2, 4, 0, 6])
        self.assertEqual(ret, "2(x^3) + 4(x^2) + 6")

    def test_zeros_end(self):
        ret = get_polynomial_string([6, 2, 0, 0])
        self.assertEqual(ret, "6(x^3) + 2(x^2)")

    def test_zero_end(self):
        ret = get_polynomial_string([2, 6, 3, 0])
        self.assertEqual(ret, "2(x^3) + 6(x^2) + 3x")

    def test_none(self):
        ret = get_polynomial_string([None])
        self.assertEqual(ret, "0")

    def test_nones(self):
        ret = get_polynomial_string([None, None])
        self.assertEqual(ret, "0")

    def test_leading_none(self):
        ret = get_polynomial_string([None, 2, 4, 6])
        self.assertEqual(ret, "2(x^2) + 4x + 6")

    def test_leading_nones(self):
        ret = get_polynomial_string([None, None, 4, 6])
        self.assertEqual(ret, "4x + 6")

    def test_nones_middle(self):
        ret = get_polynomial_string([2, None, None, 6])
        self.assertEqual(ret, "2(x^3) + 6")

    def test_none_middle(self):
        ret = get_polynomial_string([2, 4, None, 6])
        self.assertEqual(ret, "2(x^3) + 4(x^2) + 6")

    def test_nones_end(self):
        ret = get_polynomial_string([6, 2, None, None])
        self.assertEqual(ret, "6(x^3) + 2(x^2)")

    def test_none_end(self):
        ret = get_polynomial_string([2, 6, 3, 0])
        self.assertEqual(ret, "2(x^3) + 6(x^2) + 3x")

    def test_long(self):
        ret = get_polynomial_string([3, 5, 8, 2, 4, 6])
        self.assertEqual(ret, "3(x^5) + 5(x^4) + 8(x^3) + 2(x^2) + 4x + 6")

    def test_two(self):
        ret = get_polynomial_string([3, 7])
        self.assertEqual(ret, "3x + 7")

    def test_single(self):
        ret = get_polynomial_string([7])
        self.assertEqual(ret, "7")

    def test_negative(self):
        ret = get_polynomial_string([4, -2, 5, 3])
        self.assertEqual(ret, "4(x^3) - 2(x^2) + 5x + 3")

    def test_negatives(self):
        ret = get_polynomial_string([4, -2, -5, 3])
        self.assertEqual(ret, "4(x^3) - 2(x^2) - 5x + 3")

    def test_leading_negative(self):
        ret = get_polynomial_string([-9, 2, 4, 6])
        self.assertEqual(ret, "-9(x^3) + 2(x^2) + 4x + 6")

    def test_all_negatives(self):
        ret = get_polynomial_string([-9, -2, -4, -6])
        self.assertEqual(ret, "-9(x^3) - 2(x^2) - 4x - 6")

    def test_negative_end(self):
        ret = get_polynomial_string([9, 2, 4, -6])
        self.assertEqual(ret, "9(x^3) + 2(x^2) + 4x - 6")

    def test_long_negative(self):
        ret = get_polynomial_string([-3, 5, -8, 2, -4, 6])
        self.assertEqual(ret, "-3(x^5) + 5(x^4) - 8(x^3) + 2(x^2) - 4x + 6")

    def test_two_negative(self):
        ret = get_polynomial_string([-3, -7])
        self.assertEqual(ret, "-3x - 7")

    def test_single_negative(self):
        ret = get_polynomial_string([-7])
        self.assertEqual(ret, "-7")

    def test_single_one(self):
        ret = get_polynomial_string([1])
        self.assertEqual(ret, "1")

    def test_two_lone_ones(self):
        ret = get_polynomial_string([1, 1])
        self.assertEqual(ret, "x + 1")

    def test_leading_one(self):
        ret = get_polynomial_string([1, 2, 4, 6])
        self.assertEqual(ret, "x^3 + 2(x^2) + 4x + 6")

    def test_middle_one(self):
        ret = get_polynomial_string([4, 1, 4, 6])
        self.assertEqual(ret, "4(x^3) + x^2 + 4x + 6")

    def test_zeros_and_ones_middle(self):
        ret = get_polynomial_string([2, 0, 1, 6])
        self.assertEqual(ret, "2(x^3) + x + 6")

    def test_zero_middle_one_end(self):
        ret = get_polynomial_string([2, 4, 0, 1])
        self.assertEqual(ret, "2(x^3) + 4(x^2) + 1")

    def test_ones_end(self):
        ret = get_polynomial_string([6, 2, 1, 1])
        self.assertEqual(ret, "6(x^3) + 2(x^2) + x + 1")

    def test_one_middle_zero_end(self):
        ret = get_polynomial_string([2, 6, 1, 0])
        self.assertEqual(ret, "2(x^3) + 6(x^2) + x")

    def test_long_ones(self):
        ret = get_polynomial_string([1, 5, 1, 2, 1, 1])
        self.assertEqual(ret, "x^5 + 5(x^4) + x^3 + 2(x^2) + x + 1")

    def test_negative_one(self):
        ret = get_polynomial_string([4, -1, 5, 3])
        self.assertEqual(ret, "4(x^3) - x^2 + 5x + 3")

    def test_negative_ones(self):
        ret = get_polynomial_string([4, -1, -1, 3])
        self.assertEqual(ret, "4(x^3) - x^2 - x + 3")

    def test_leading_negative_one(self):
        ret = get_polynomial_string([-1, 2, 4, 6])
        self.assertEqual(ret, "-x^3 + 2(x^2) + 4x + 6")

    def test_all_negative_ones(self):
        ret = get_polynomial_string([-1, -1, -1, -1])
        self.assertEqual(ret, "-x^3 - x^2 - x - 1")

    def test_negative_one_end(self):
        ret = get_polynomial_string([9, 2, 4, -1])
        self.assertEqual(ret, "9(x^3) + 2(x^2) + 4x - 1")

    def test_long_negative_ones(self):
        ret = get_polynomial_string([-1, 5, -1, 2, -1, 6])
        self.assertEqual(ret, "-x^5 + 5(x^4) - x^3 + 2(x^2) - x + 6")

    def test_two_negative_ones(self):
        ret = get_polynomial_string([-1, -1])
        self.assertEqual(ret, "-x - 1")

    def test_single_negative_one(self):
        ret = get_polynomial_string([-1])
        self.assertEqual(ret, "-1")

    def test_leading_zero_then_negative_one(self):
        ret = get_polynomial_string([0, -1, 4, 6])
        self.assertEqual(ret, "-x^2 + 4x + 6")

    def test_negative_and_positive_ones(self):
        ret = get_polynomial_string([-1, 1, -1, 1])
        self.assertEqual(ret, "-x^3 + x^2 - x + 1")

    def test_zero_and_negative_one_middle(self):
        ret = get_polynomial_string([2, 0, -1, 6])
        self.assertEqual(ret, "2(x^3) - x + 6")

    def test_zero_middle_negative_one_end(self):
        ret = get_polynomial_string([2, 4, 0, -1])
        self.assertEqual(ret, "2(x^3) + 4(x^2) - 1")

    def test_negative_ones_end(self):
        ret = get_polynomial_string([6, 2, -1, -1])
        self.assertEqual(ret, "6(x^3) + 2(x^2) - x - 1")

    def test_negative_one_middle_zero_end(self):
        ret = get_polynomial_string([2, 6, -1, 0])
        self.assertEqual(ret, "2(x^3) + 6(x^2) - x")


if __name__ == '__main__':
    unittest.main()
