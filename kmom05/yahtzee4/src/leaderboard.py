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

    def load(self, filename="leaderboard.txt"):
        """
        Läser in leaderboard.txt och laddar spelardata i UnorderedList.
        """
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    name, score = line.strip().split(": ")
                    self.players.add((name, int(score)))
        except FileNotFoundError:
            pass

    def add_player(self, name, score):
        """
        Lägger till en spelare i en tuple.
        """
        self.players.add((name, score))

    def remove_player(self, name):
        """
        Tar bort en spelare från listan genom att använda remove()
        istället för att direkt hantera head.
        """
        try:
            for i in range(self.players.size()):
                player = self.players.get(i)
                if player[0] == name:
                    self.players.remove(player)
                    return
            raise ValueError("Spelaren finns inte i listan.")
        except ValueError as e:
            print(f"Fel: {e}")

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
            for name, score in self.players:
                f.write(f"{name}: {score}\n")

    def get_players(self):
        """
        Returnerar en lista med tuples av spelarnamn och poäng.
        """
        return list(self.players)
