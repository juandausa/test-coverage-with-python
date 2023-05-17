import unittest
from .calculator import Calculator

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        assert self.calculator.add(1, 2) == 3.0
        assert self.calculator.add(1.0, 2.0) == 3.0
        assert self.calculator.add(0, 2.0) == 2.0
        assert self.calculator.add(2.0, 0) == 2.0
        assert self.calculator.add(-4, 2.0) == -2.0

    def test_add_two_positive_integeres(self):
        assert self.calculator.add(1, 2) == 3.0

    def test_add_is_a_conmutative_operation(self):
        assert self.calculator.add(1, 2) == self.calculator.add(2, 1)

    def test_add_two_negative_integeres(self):
        assert self.calculator.add(-1, -2) == -3.0

    def test_add_positive_integere_and_zero(self):
        assert self.calculator.add(1, 0) == 1.0

    def test_subtract(self):
        assert self.calculator.subtract(1, 2) == -1.0
        assert self.calculator.subtract(2, 1) == 1.0
        assert self.calculator.subtract(1.0, 2.0) == -1.0
        assert self.calculator.subtract(0, 2.0) == -2.0
        assert self.calculator.subtract(2.0, 0.0) == 2.0
        assert self.calculator.subtract(-4, 2.0) == -6.0

    def test_multiply(self):
        assert self.calculator.multiply(1, 2) == 2.0
        assert self.calculator.multiply(1.0, 2.0) == 2.0
        assert self.calculator.multiply(0, 2.0) == 0.0
        assert self.calculator.multiply(2.0, 0.0) == 0.0
        assert self.calculator.multiply(-4, 2.0) == -8.0

    def test_pow_power_zero(self):
        assert self.calculator.pow(1, 0) == 1.0

    def test_pow_positive_base_and_power(self):
        assert self.calculator.pow(2, 3) == 8.0

    def test_pow_positive_base_and_power(self):
        assert self.calculator.pow(2, 3) == 8.0

    #def test_pow_positive_base_and_negative_power(self):
        # assert self.calculator.pow(4, -1) == 2

    def test_divide(self):
        assert self.calculator.divide(1, 2) == 0.5
        assert self.calculator.divide(1.0, 2.0) == 0.5
        assert self.calculator.divide(0, 2.0) == 0
        assert self.calculator.divide(-4, 2.0) == -2.0
        # assert self.calculator.divide(2.0, 0.0) == 'Cannot divide by 0'
