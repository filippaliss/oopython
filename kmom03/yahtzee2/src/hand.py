
"""
Module to define the Hand class.
"""
from src.die import Die

class Hand():
    """
    A class representing a hand of dice for the game of Yahtzee.
    """

    def __init__(self, dice_values=None):
        """
        list of values for dice. else random values.

        """
        if dice_values is None:
            self.dice = [Die() for _ in range(5)]
        else:
            self.dice = [Die(value) for value in dice_values]

    def roll(self, indexes=None):
        """
        Rolls the dice in the hand.

        Args:
            indexes (list, optional): List of indices specifying
            which dice to roll. If not provided, all dice are rolled.
        """
        if indexes is None:
            for die in self.dice:
                die.roll()
        else:
            for index in indexes:
                self.dice[index].roll()

    def __str__(self):
        """
        Returns a string.

        Returns:
            str: ', 'seperating the string of dice values in the hand.
        """
        return ", ".join(str(die.get_value()) for die in self.dice)
