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

        pass

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
    def __init__(self):
        self.name = "Three of a kind"

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
    def __init__(self):
        self.name = "Four of a kind"

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
    def __init__(self):
        self.name = "Small straight"
    
    def points(self, hand: Hand) -> int:
        values = sorted(set(die.get_value() for die in hand.dice))

        small_straight = [
            [1, 2, 3, 4],
            [2, 3, 4, 5],
            [3, 4, 5, 6]
        ]
        
        for straight in small_straight:
            if all (num in values for num in straight):
                return 30
            return 0

class LargeStraight(Rule):
    def __init__(self):
        self.name = "Large straight"
    
    def points(self, hand: Hand) -> int:
        values = sorted(set(die.get_value() for die in hand.dice))

        large_straight = [
            [1, 2, 3, 4, 5],
            [2, 3, 4, 5, 6]
        ]
        
        for straight in large_straight:
            if all (num in values for num in straight):
                return 40
            return 0

class Yahtzee(Rule):
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
    def __init__(self):
        self.name = "Chance"

    def points(self, hand: Hand) -> int:
        return sum(die.get_value() for die in hand.dice)