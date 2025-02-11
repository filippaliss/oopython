"""
Module to define unit tests for the Hand class.
"""
import unittest
import random
from src.hand import Hand

class TestHand(unittest.TestCase):
    """
    A test suite for the Hand class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        random.seed(42)

    def test_create_hand_without_arguments(self):
        """
        Test creating a hand without providing arguments.
        """
        hand = Hand()

        self.assertIsInstance(hand, Hand)
        self.assertEqual(len(hand.dice), 5)

        expected_values = [6, 1, 1, 6, 3]
        actual_values = hand.to_list()
        self.assertEqual(actual_values, expected_values)


    def test_create_hand_with_list_of_values(self):
        """
        Test creating a Hand object with an explicit list of dice values.
        """
        dice_values = [2, 4, 6, 1, 3]
        hand = Hand(dice_values)

        self.assertEqual(hand.to_list(), dice_values)

    def test_to_list_returns_correct_values(self):
        """
        Test if to_list() correctly returns a list of dice values.
        """
        dice_values = [1, 3, 5, 2, 6]
        hand = Hand(dice_values)

        self.assertEqual(hand.to_list(), dice_values)

if __name__ == '__main__':
    unittest.main()
