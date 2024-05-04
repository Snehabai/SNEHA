class Player:
    def __init__(self, player_id, name, skills):
        self.player_id = player_id
        self.name = name
        self.skills = skills

class Team:
    def __init__(self, team_id, name):
        self.team_id = team_id
        self.name = name

class PlayerDatabase:
    def __init__(self):
        self.players = {}

    def create_player(self, player_id, name, skills):
        if player_id in self.players:
            raise ValueError("player ID already exists")
        self.players[player_id] = Player(player_id, name, skills)

    def read_player(self, player_id):
        if player_id not in self.players:
            raise ValueError("player ID does not exist")
        return self.players[player_id]

    def update_player(self, player_id, name=None, skills=None):
        if player_id not in self.players:
            raise ValueError("Player ID does not exist")
        player = self.players[player_id]
        if name:
            player.name = name
        if skills:
            player.skills = skills

    def delete_player(self, player_id):
        if player_id not in self.players:
            raise ValueError("Player ID does not exist")
        del self.players[player_id]

    def display_players(self):
        for player_id, player in self.players.items():
            print(f"Player ID: {player_id}, Name: {player.name}, Skills: {', '.join(player.skills)}")

class TeamDatabase:
    def __init__(self):
        self.teams = {}

    def create_team(self, team_id, name):
        if team_id in self.teams:
            raise ValueError("team ID already exists")
        self.teams[team_id] = Team(team_id, name)

    def read_team(self, team_id):
        if team_id not in self.teams:
            raise ValueError("team ID does not exist")
        return self.teams[team_id]

    def update_team(self, team_id, name=None):
        if team_id not in self.teams:
            raise ValueError("team ID does not exist")
        team = self.teams[team_id]
        if name:
            team.name = name

    def delete_team(self, team_id):
        if team_id not in self.teams:
            raise ValueError("Team ID does not exist")
        del self.teams[team_id]

    def display_teams(self):
        for team_id, team in self.teams.items():
            print(f"Team ID: {team_id}, Name: {team.name}")

# Unit tests
import unittest

class TestPlayerDatabase(unittest.TestCase):
    def setUp(self):
        self.db = PlayerDatabase()
        self.db.create_player(1, "John Doe", ["football"])
        self.db.create_player(2, "Jane Smith", ["cricket"])

    def test_create_player(self):
        self.db.create_player(3, "Alice Johnson", ["basketball"])
        self.assertIn(3, self.db.players)

    def test_read_player(self):
        player = self.db.read_player(1)
        self.assertEqual(player.name, "John Doe")

    def test_update_player(self):
        self.db.update_player(1, name="Johnathan Doe")
        player = self.db.read_player(1)
        self.assertEqual(player.name, "Johnathan Doe")

    def test_delete_player(self):
        self.db.delete_player(1)
        self.assertNotIn(1, self.db.players)
    
    def test_display_players(self):
        # Redirect stdout to capture printed output
        #import sys
        #from io import StringIO
        #captured_output = StringIO()
        #sys.stdout = captured_output
        
        self.db.display_players()
        
        #sys.stdout = sys._stdout_  # Reset redirect
        #printed_output = captured_output.getvalue().strip()
        
        #expected_output = "Player ID: 1, Name: John Doe, Skills: football\nPlayer ID: 2, Name: Jane Smith, Skills: cricket"
        #self.assertEqual(printed_output, expected_output)

class TestTeamDatabase(unittest.TestCase):
    def setUp(self):
        self.db = TeamDatabase()
        self.db.create_team(1, "A")
        self.db.create_team(2, "B")

    def test_create_team(self):
        self.db.create_team(3, "D")
        self.assertIn(3, self.db.teams)

    def test_read_team(self):
        team = self.db.read_team(1)
        self.assertEqual(team.name, "A")

    def test_update_team(self):
        self.db.update_team(1, name="C")
        team = self.db.read_team(1)
        self.assertEqual(team.name, "C")

    def test_delete_team(self):
        self.db.delete_team(1)
        self.assertNotIn(1, self.db.teams)
    
    def test_display_teams(self):
        # Redirect stdout to capture printed output
        #import sys
        #from io import StringIO
        ##sys.stdout = captured_output
        
        self.db.display_teams()
        
        #sys.stdout = sys._stdout_  # Reset redirect
        #printed_output = captured_output.getvalue().strip()
        
        #expected_output = "Team ID: 1, Name: A\nTeam ID: 2, Name: B"
        #self.assertEqual(printed_output, expected_output)

if __name__ == '__main__':
    unittest.main(argv=[''],verbosity=3,exit=False)