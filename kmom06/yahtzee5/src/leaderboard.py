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
        Hanterar felaktiga rader och saknad fil.
        """
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(": ")
                    if len(parts) == 2:
                        name, score = parts
                        try:
                            self.players.add((name, int(score)))
                        except ValueError:
                            print(f"Ogiltigt poängvärde, hoppar över: {line.strip()}")
                    else:
                        print(f"Felaktigt format, hoppar över: {line.strip()}")
        except FileNotFoundError:
            pass

    def add_player(self, name, score):
        """
        Lägger till en spelare i en tuple.
        """
        self.players.add((name, score))

    def remove_player(self, name):
        """
        ta bort en spelare
        """
        current = self.players.head
        previous = None

        while current:
            if current.value[0] == name:
                if previous is None:
                    self.players.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
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

    def get_players(self):
        """
        Returnerar en lista med tuples av spelarnamn och poäng.
        """
        players = []
        current = self.players.head
        while current:
            players.append(current.value)  # Varje node i listan innehåller en tuple (name, score)
            current = current.next
        return players
