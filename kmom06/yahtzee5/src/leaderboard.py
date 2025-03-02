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
            Lägger till en spelare i en tuple
        """
        self.players.add((name, score))

    def remove_player(self, name):
        """
            Tar bort en spelare från listan baserat på namn
        """
        for player in self.players.items:
            if player[0] == name:
                self.players.remove(player)
                break

    def get_top_players(self):
        """
            Sortera spelarna
        """
        sorted_players = self.sort_players_by_score(self.players.items)
        return sorted_players

    def sort_players_by_score(self, players):
        """
        Sortera spelarna baserat på poäng i fallande ordning.
        """
        players_list = []
        current = players.head
        while current:
            players_list.append(current.data)
            current = current.next
        return sorted(players_list, key=self.get_score, reverse=True)

    def get_score(self, player):
        """
            Hämtar poängen för en spelare (som är den andra värdet i tuplen)
        """
        return player[1]

    def save_to_file(self):
        """
            Spara leaderboarden till en fil
        """
        with open("leaderboard.txt", "w", encoding="utf-8") as f:
            for player in self.players.items:
                f.write(f"{player[0]}: {player[1]}\n")
