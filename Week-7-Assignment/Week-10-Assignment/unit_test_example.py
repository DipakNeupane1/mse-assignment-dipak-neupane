# Week 11 - Activity 1: Unit testing
# Develop a test unit for the *, -, / and % functions and add it to the below example.
# Once completed, please push your updated code to GitHub and share it here.


import unittest


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def subtract(x, y):
    return x - y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return None


def modulo(x, y):
    if y != 0:
        return x % y
    else:
        return None


class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertIsNone(divide(10, 0))  # Test division by zero and assert it as None.

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(10, 2), 0)
        self.assertIsNone(modulo(10, 0))  # Test modulo by zero and assert it as None.


if __name__ == "__main__":
    unittest.main()
