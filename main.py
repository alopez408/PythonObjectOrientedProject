class Player:
    def __init__(self, player_name, player_position):
        self.player_name = player_name
        self.player_position = player_position

    def __str__(self):
        return f"{self.player_name} ({self.player_position})"

class NFLTeam:
    def __init__(self, team_name, player_list):
        self.team_name = team_name
        self.player_list = player_list

    def print_team_info(self):
        print(f"Team: {self.team_name}")
        print("Players:")
        for player in self.player_list:
            print(f" - {player}")

# create players
player1 = Player("Joe Montana", "QB")
player2 = Player("Barry Sanders", "RB")
player3 = Player("Jerry Rice", "WR")
player4 = Player("Graham Gano", "K")

# add players to a list
playerList = [player1, player2, player3, player4]

# create NFL team
team = NFLTeam("Smashmouth Football", playerList)

# output the team name and player list
team.print_team_info()
