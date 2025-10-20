#!/usr/bin/env python3
"""
Unit tests for the Calculator application
Run with: python -m pytest test_calculator.py
Or: python test_calculator.py
"""

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(10, 20), 30)

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)

    def test_add_zero(self):
        """Test addition with zero."""
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_add_floats(self):
        """Test addition with floating point numbers."""
        self.assertAlmostEqual(self.calc.add(2.5, 3.7), 6.2)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(20, 5), 15)

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(10, -5), 15)

    def test_subtract_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(10, 10), 100)

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.multiply(-5, -3), 15)

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_multiply_floats(self):
        """Test multiplication with floating point numbers."""
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertAlmostEqual(self.calc.multiply(0.5, 0.5), 0.25)

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(20, 4), 5)

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_divide_floats(self):
        """Test division with floating point numbers."""
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.333333, places=5)

    def test_divide_by_zero(self):
        """Test that division by zero raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    def test_calculate_add(self):
        """Test calculate method with addition."""
        self.assertEqual(self.calc.calculate('+', 5, 3), 8)

    def test_calculate_subtract(self):
        """Test calculate method with subtraction."""
        self.assertEqual(self.calc.calculate('-', 10, 3), 7)

    def test_calculate_multiply(self):
        """Test calculate method with multiplication."""
        self.assertEqual(self.calc.calculate('*', 5, 3), 15)

    def test_calculate_divide(self):
        """Test calculate method with division."""
        self.assertEqual(self.calc.calculate('/', 10, 2), 5)

    def test_calculate_invalid_operation(self):
        """Test that invalid operation raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.calculate('%', 10, 3)
        self.assertIn("Unsupported operation", str(context.exception))

    def test_calculate_divide_by_zero(self):
        """Test that calculate method handles division by zero."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.calculate('/', 10, 0)


class TestCalculatorEdgeCases(unittest.TestCase):
    """Test edge cases for the Calculator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_very_large_numbers(self):
        """Test operations with very large numbers."""
        large = 10**15
        self.assertEqual(self.calc.add(large, large), 2 * large)
        self.assertEqual(self.calc.multiply(large, 2), 2 * large)

    def test_very_small_numbers(self):
        """Test operations with very small numbers."""
        small = 10**-15
        self.assertAlmostEqual(self.calc.add(small, small), 2 * small)

    def test_precision(self):
        """Test floating point precision."""
        # Known floating point precision issue
        result = self.calc.add(0.1, 0.2)
        self.assertAlmostEqual(result, 0.3, places=10)


def run_tests():
    """Run all tests."""
    unittest.main(verbosity=2)


if __name__ == '__main__':
    run_tests()
