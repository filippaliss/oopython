"""
leaderboard filen, Hålla reda på spelarnas namn och poäng i en leaderboard.
"""
class Leaderboard:
    def __init__(self):
        self.players = UnordedList()

    def add_player(self, name, score):
        """
            Lägger till en spelare i en tuple
        """
        self.player.add((name, score))

    def remove_player(self, name):
        """
            Tar bort en spelare från listan baserat på namn
        """
        for player in self.player.itmes:
            if player[0] == name:
                self.player.remove(player)
                break

    def get_top_players(self):
        """
            Sortera spelarna utan att använda lambda
        """
        sorted_players = self.sort_players_by_score(self.players.items)
        return sorted_players

    def sort_players_by_score(self, players):
        """
            Sortera spelarna baserat på poäng i fallande ordning
        """
        return sorted(players, key=self.get_score, reverse=True)

    def get_score(self, player):
        """
            Hämtar poängen för en spelare (som är den andra värdet i tuplen)
        """
        return player[1]

    def save_to_file(self):
        """
            Spara leaderboarden till en fil
        """
        with open("leaderboard.txt", "w") as f:
            for player in self.players.items:
                f.write(f"{player[0]}: {player[1]}\n")