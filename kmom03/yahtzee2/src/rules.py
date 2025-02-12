"""
rule filen, med alla regler till yahtzeet.
"""
from abc import ABC, abstractmethod
from src.hand import Hand

class Rule(ABC):
    """
    Abstrakt klass för regler för poäng.
    """
    @abstractmethod
    def points(self, hand: Hand) -> int:
        """
        denna skall vara tom men används till alla regler för poängräkning.
        """


class SameValueRule(Rule):
    """
    räknar värdet och retunerar hur många av det efterfrågade vädret som slogs.
    """
    def __init__(self, value: int, name: str):
        self.value = value
        self.name = name

    def points(self, hand: Hand) -> int:
        return sum(die.get_value()
            for die in hand.dice if die.get_value() == self.value)

class Ones(SameValueRule):
    """
    Rule för att räkna ettor.
    """
    def __init__(self):
        super().__init__(1, "Ones")

class Twos(SameValueRule):
    """
    Rule för att räkna tvåor.
    """
    def __init__(self):
        super().__init__(2, "Twos")

class Threes(SameValueRule):
    """
    Rule för att räkna treor.
    """
    def __init__(self):
        super().__init__(3, "Threes")

class Fours(SameValueRule):
    """
    Rule för att räkna fyror.
    """
    def __init__(self):
        super().__init__(4, "Fours")

class Fives(SameValueRule):
    """
    Rule för att räkna femmor.
    """
    def __init__(self):
        super().__init__(5, "Fives")

class Sixes(SameValueRule):
    """
    Rule för att räkna sexor.
    """
    def __init__(self):
        super().__init__(6, "Sixes")

class ThreeOfAKind(Rule):
    """
    rule four of a kind, kollar om man får 3 av samma,
    gör inget skillnad på total summan.
    """
    def __init__(self):
        self.name = "Three Of A Kind"

    def points(self, hand: Hand) -> int:

        counts = {}

        for die in hand.dice:
            value = die.get_value()
            if value in counts:
                counts[value] += 1
            else:
                counts[value] = 1

        for count in counts.values():
            if count >= 3:
                return sum(die.get_value() for die in hand.dice)

        return 0

class FourOfAKind(Rule):
    """
    rule four of a kind, kollar om man får fyra av samma,
    gör inget skillnad på total summan.
    """
    def __init__(self):
        self.name = "Four Of A Kind"

    def points(self, hand: Hand) -> int:

        counts = {}

        for die in hand.dice:
            value = die.get_value()
            if value in counts:
                counts[value] += 1
            else:
                counts[value] = 1

        for count in counts.values():
            if count >= 4:
                return sum(die.get_value() for die in hand.dice)

        return 0

class FullHouse(Rule):
    """
    rule fullhouse kollar om man får 2 av samma samt 3 av samma på ett kasst.
    """
    def __init__(self):
        self.name = "Full House"

    def points(self, hand: Hand) -> int:

        counts = {}

        for die in hand.dice:
            value = die.get_value()
            counts[value] = counts.get(value, 0) + 1
        if sorted(counts.values()) == [2, 3]:
            return 25
        return 0

class SmallStraight(Rule):
    """
    rule smallstraight kollar om man får 4 i nummer ordning.
    """
    def __init__(self):
        self.name = "Small Straight"

    def points(self, hand: Hand) -> int:
        values = sorted(set(die.get_value() for die in hand.dice))

        small_straight = [
            {1, 2, 3, 4},
            {2, 3, 4, 5},
            {3, 4, 5, 6}
        ]

        for straight in small_straight:
            if  straight.issubset(values):
                return 30
        return 0

class LargeStraight(Rule):
    """
    rule large straight kollar om man får en stor/liten steg (svenska regler)
    """
    def __init__(self):
        self.name = "Large Straight"

    def points(self, hand: Hand) -> int:
        values = sorted(set(die.get_value() for die in hand.dice))

        if values in ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]):
            return 40
        return 0

class Yahtzee(Rule):
    """
    yahtzee rule, kollar om tärningarna slår 5 av samma.
    """
    def __init__(self):
        self.name = "Yahtzee"

    def points(self, hand: Hand) -> int:

        counts = {}

        for die in hand.dice:
            value = die.get_value()
            if value in counts:
                counts[value] += 1
            else:
                counts[value] = 1

        for count in counts.values():
            if count >= 5:
                return 50

        return 0

class Chance(Rule):
    """
    chance rule där ett kast blir chance och alla poäng sätts.
    """
    def __init__(self):
        self.name = "Chance"

    def points(self, hand: Hand) -> int:
        return sum(die.get_value() for die in hand.dice)
