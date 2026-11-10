# https://github.com/felipeg1234/lab10-FG-SI
# Partner 1: Felipe Gaitan
# Partner 2: Seth Imig

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        assert add(2, 2) == 4

    def test_subtract(self):
        assert sub(2, 2) == 0

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 2)

    def test_logarithm(self):
        assert log(8, 2) == 3

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(0, 2)

    def test_multiply(self):
        assert multiply(1, 2) == 2

    def test_divide(self):
        assert divide(2, 1) == 2

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        assert hypotenuse(0, 2) == 2

    def test_sqrt(self): 
        with self.assertRaises(ValueError):
            square_root(-1)
        assert square_root(4) == 2

    # Do not touch this
    if __name__ == "__main__":
        unittest.main()

# Do not touch this
if __name__ == "__main__":
    unittest.main()