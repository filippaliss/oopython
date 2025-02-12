"""
module that defines the Scoreboard class
"""
class Scoreboard:
    def __init__(self):
        self.scores = {}

    def get_total_points(self) -> int:
        """
        Returns the total points accumulated
        """
        return sum (self.scores.values())

    def add_points(self, rule_name: str, hand) -> None:
        """
        Adds points to the scoreboard based on the rule and hand
        """
        points = hand.calculate_points(rule_name)
        self.scores[rule_name] = points

    def get_points(self, rule_name: str) -> int:
        """
        Returns the points for a specific rule.
        """
        return self.scores.get(rule_name, 0)

    def finished(self) -> bool:
        """
        Returns True if all required rules have been scored.
        """
        required_rules = {"ThreeOfAKind", "FourOfAKind", "FullHouse", "SmallStraight", "LargeStraight", "Yahtzee", "Chance"}  
        return required_rules.issubset(self.scores.keys())

    @classmethod
    def from_dict(cls, points: dict[str, int]) -> 'Scoreboard':
        """
        Creates a Scoreboard instance from a dictionary.
        """
        scoreboard = cls()
        scoreboard.scores = points
        return scoreboard
