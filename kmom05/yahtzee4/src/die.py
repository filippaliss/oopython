"""
Module to define the Die class.
"""

import random

class Die():
    """
    A class representing a six-sided die.
    """

    MIN_ROLL_VALUE = 1
    MAX_ROLL_VALUE = 6

    @property
    def value(self):
        """Getter för att hämta värdet på tärningen"""
        return self._value

    def __init__(self, value=None):
        """
        Initializes a Die object.
        """
        if value is None:
            self._value = random.randint(self.MIN_ROLL_VALUE, self.MAX_ROLL_VALUE)
        else:
            self._value = min(max(value, self.MIN_ROLL_VALUE), self.MAX_ROLL_VALUE)

    def get_name(self):
        """
        Returns the name of the die's current value.
        """
        return {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six'
        }[self._value]

    def get_value(self):
        """
        Returns the current value of the die.
        """
        return self._value

    def roll(self):
        """
        Rolls the die, updating its value to a random number between
        MIN_ROLL_VALUE and MAX_ROLL_VALUE.
        """
        self._value = random.randint(self.MIN_ROLL_VALUE, self.MAX_ROLL_VALUE)

    def __str__(self):
        """
        Returns a string representation of the die's current value.
        """
        return str(self._value)

    def __eq__(self, other):
        """
        Function accepts either a Die object or an integer.
        It returns True if the dice show the same value, or if the
        integer matches the die's value. Otherwise, it returns False.
        """
        if isinstance(other, Die):
            return self._value == other.value
        if isinstance(other, int):
            return self._value == other
        return False
