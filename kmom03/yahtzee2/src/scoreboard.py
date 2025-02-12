"""
module that defines the Scoreboard class
"""
from src.rules import (
    Ones, Twos, Threes, Fours, Fives, Sixes,
    ThreeOfAKind, FourOfAKind, FullHouse, SmallStraight,
    LargeStraight, Yahtzee, Chance)

class Scoreboard:
    """
    A class representing the Scoreboard for the game of Yahtzee.
    """
    def __init__(self):
        self.scores = {}
        self.rules = {
            "Ones": Ones(), "Twos": Twos(), "Threes": Threes(),
            "Fours": Fours(), "Fives": Fives(), "Sixes": Sixes(),
            "Three Of A Kind": ThreeOfAKind(), "Four Of A Kind": FourOfAKind(),
            "Full House": FullHouse(), "Small Straight": SmallStraight(),
            "Large Straight": LargeStraight(), "Yahtzee": Yahtzee(), "Chance": Chance()
        }

    def get_total_points(self) -> int:
        """
        Returnerar den totala summan av alla poäng.
        """
        return sum(score for score in self.scores.values() if score >= 0)

    def add_points(self, rule_name, hand):
        """
        Lägger till poäng för en viss regel baserat på en given Hand.
        """
        if self.scores.get(rule_name, -1) != -1:
            raise ValueError(f"Points for {rule_name} can not change.")

        rule = self.rules.get(rule_name)
        if rule:
            self.scores[rule_name] = rule.points(hand)

    def get_points(self, rule_name: str) -> int:
        """
        Returnerar poängen för en specifik regel.
        """
        return self.scores.get(rule_name, 0)

    def finished(self) -> bool:
        """
        Returnerar True om alla regler har fått poäng.
        """
        return all(rule in self.scores and self.scores[rule] >= 0 for rule in self.rules)

    @classmethod
    def from_dict(cls, points: dict[str, int]) -> 'Scoreboard':
        """
        Skapar en Scoreboard-instans från en dictionary med poäng.
        """
        scoreboard = cls()
        scoreboard.scores = points
        return scoreboard
