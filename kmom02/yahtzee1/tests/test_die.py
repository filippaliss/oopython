"""
Module to define unit tests for the Die class.
"""
import unittest
import random
from src.die import Die

class TestDie(unittest.TestCase):
    """
    A test suite for the Die class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        # Set a fixed seed for reproducibility
        random.seed(42)

    def test_create_die_without_arguments(self):
        """
        Test creating a die without initial arguments.
        """
        die = Die()
        self.assertIsInstance(die, Die)
        self.assertIs(die.get_value(), range(1, 7))

    def test_create_die_with_initial_value(self):
        """
        Test creating a die with an initial value.
        """
        die = Die(3)
        self.assertEqual(die.get_value(), 3)

    def test_create_die_with_invalid_value(self):
        """
        Test creating a die with an invalid initial value.
        """
        die = Die(100)
        self.assertEqual(die.get_value(), 6)

    def test_roll_changes_value(self):
        """
        Test if rolling the die changes its value.
        """
        die = Die()
        initial_value = die.get_value()
        die.roll()
        new_value = die.get_value()
        self.assertNotEqual(initial_value, new_value)

    def test_get_name_returns_correct_name(self):
        """
        Test if get_name returns the correct name for the die's value.
        """
        die = Die()
        self.assertEqual(die.get_name(), "six")

    def test_get_first_roll_correct(self):
        """
        Test if expected_values == actual_values.
        """
        die = Die()
        expected_values = [1,1,6,3,2]
        actual_values = []
        print(" ")
        for _ in range(5):
            die.roll()
            actual_values.append(die.get_value())

        self.assertEqual(actual_values, expected_values)

if __name__ == '__main__':
    unittest.main()
