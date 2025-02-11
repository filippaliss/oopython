
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
        self.dice = []

        if dice_values is None:
            for _ in range (5):
                self.dice.append(Die())
        else:
            for value in dice_values:
                self.dice.append(Die(value))

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
        values = []
        for die in self.dice:
            values.append(str(die.get_value()))

        return ", ".join(values)

    def to_list(self):
        """
        Return a list contaning the values(integers) of all the dice
        in the Hand object
        """
        result = []
        for die in self.dice:
            result.append(die._value)
        return result