"""
leaderboard filen, Hålla reda på spelarnas namn och poäng i en leaderboard.
"""
from src.unorderedlist import UnorderedList

class Leaderboard:
    """
    Hantera leaderboarden genom att lagra, sortera och spara spelare baserat på poäng.
    """
    def __init__(self):
        self.players = UnorderedList()

    def add_player(self, name, score):
        """
        Lägger till en spelare i en tuple.
        """
        self.players.add((name, score))

    def remove_player(self, name):
        """
        Tar bort en spelare från listan baserat på namn.
        """
        current = self.players.head
        while current:
            if current.value[0] == name:
                self.players.remove(current.value)
                return
            current = current.next

    def get_score(self, player):
        """
        Hämtar poängen för en spelare (som är den andra värdet i tuplen).
        """
        return player[1]

    def save_to_file(self):
        """
        Spara leaderboarden till en fil.
        """
        with open("leaderboard.txt", "w", encoding="utf-8") as f:
            current = self.players.head
            while current:
                f.write(f"{current.value[0]}: {current.value[1]}\n")
                current = current.next
