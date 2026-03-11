import unittest

def multiply_numbers(num1, num2):
    """
    Returns the product of two numbers.
    
    Args:
        num1 (int or float): The first number.
        num2 (int or float): The second number.
    
    Returns:
        int or float: The product of num1 and num2.
    """
    return num1 * num2

class TestMultiplyFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply_numbers(2, 3), 6)
    
    def test_negative_numbers(self):
        self.assertEqual(multiply_numbers(-2, 3), -6)
    
    def test_zero(self):
        self.assertEqual(multiply_numbers(0, 5), 0)

if __name__ == '__main__':
    unittest.main()