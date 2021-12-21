import unittest
from calculator import router, add, minus, multiply, divide, power

class CalculatorTestCase(unittest.TestCase):
    def test_router_invalidFormat(self):
        expected = "Not in a valid format\nPlease try again\n"
        actual = router("5+6")
        self.assertEqual(expected, actual)

    def test_router_validAdd(self):
        expected = 5 + 6
        actual = router("5 + 6")
        self.assertEqual(expected, actual)

    def test_router_validMinus(self):
        expected = 5 - 6
        actual = router("5 - 6")
        self.assertEqual(expected, actual)

    def test_router_validMultiply(self):
        expected = 5 * 6
        actual = router("5 * 6")
        self.assertEqual(expected, actual)

    def test_router_validDivide(self):
        expected = 5 / 6
        actual = router("5 / 6")
        self.assertEqual(expected, actual)

    def test_router_validPower(self):
        expected = 5 ** 6
        actual = router("5 ** 6")
        self.assertEqual(expected, actual)

    def test_add(self):
        expected = 5 + 6
        actual = add([5, 6])
        self.assertEqual(expected, actual)

    def test_minus(self):
        expected = 5 - 6
        actual = minus([5, 6])
        self.assertEqual(expected, actual)

    def test_multiply(self):
        expected = 5 * 6
        actual = multiply([5, 6])
        self.assertEqual(expected, actual)

    def test_divide(self):
        expected = 5 / 6
        actual = divide([5, 6])
        self.assertEqual(expected, actual)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5/0)

    def test_power(self):
        expected = 5 ** 6
        actual = power([5, 6])
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()