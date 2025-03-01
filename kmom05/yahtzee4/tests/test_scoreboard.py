"""
Module to define unit tests for the Scoreboard class.
"""
import unittest
from unittest.mock import MagicMock
from src.scoreboard import Scoreboard

class TestScoreboard(unittest.TestCase):
    """
    A test suite for the Scoreboard class.
    """

    def setUp(self):
        """
        Set up a fresh Scoreboard instance before each test.
        """
        self.scoreboard = Scoreboard()

    def test_add_points_valid(self):
        """
        Test that points are added correctly for a rule.
        """
        mock_hand = [1, 1, 1, 1, 1]
        self.scoreboard.rules["Ones"].points = MagicMock(return_value=5)

        self.scoreboard.add_points("Ones", mock_hand)

        self.assertEqual(self.scoreboard.get_points("Ones"), 5)

    def test_add_points_duplicate(self):
        """
        Test that trying to add points for an already filled rule raises a ValueError.
        """
        mock_hand = [1, 1, 1, 1, 1]
        self.scoreboard.rules["Ones"].points = MagicMock(return_value=5)
        self.scoreboard.add_points("Ones", mock_hand)

        with self.assertRaises(ValueError):
            self.scoreboard.add_points("Ones", mock_hand)

if __name__ == "__main__":
    unittest.main()
