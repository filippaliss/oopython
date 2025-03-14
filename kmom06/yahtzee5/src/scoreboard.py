"""
module that defines the Scoreboard class
"""
import json
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
        self.players = {}
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
        total = 0
        for scores in self.scores.values():
            if scores >= 0:
                total += scores
        return total

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
        for rule in self.rules:
            if rule not in self.scores or self.scores[rule] < 0:
                return False
        return True

    @classmethod
    def from_dict(cls, points: dict[str, int]) -> 'Scoreboard':
        """
        Skapar en Scoreboard-instans från en dictionary med poäng.
        """
        scoreboard = cls()
        scoreboard.scores = points
        return scoreboard

    def available_rules(self):
        """
        Returns a list of rules that haven't been used yet.
        """
        return [rule for rule, value in self.rules.items() if value is None]

    def to_json(self):
        """
        dump score
        """
        return json.dumps(self.scores)

    @classmethod
    def from_json(cls, json_data):
        """
        Deserialisering: omvandla JSON tillbaka till ett Scoreboard-objekt.
        Om json_data redan är en dictionary, använd den direkt.
        """
        if isinstance(json_data, str):  # Om det är en JSON-sträng, omvandla till dictionary
            data = json.loads(json_data)
        elif isinstance(json_data, dict):  # Om det redan är en dictionary, använd direkt
            data = json_data
        else:
            raise TypeError("Invalid data format for Scoreboard.from_json")

        scoreboard = cls()
        scoreboard.scores = data
        return scoreboard

    def add_players(self, player_names):
        """
        Skapar ett Scoreboard för varje spelare.
        """
        self.players = {name: Scoreboard() for name in player_names}
