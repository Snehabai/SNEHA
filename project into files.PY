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

class UserInterface:
    def __init__(self, output_file="output.txt"):
        self.player_db = PlayerDatabase()
        self.team_db = TeamDatabase()
        self.MAX_PLAYERS_PER_TEAM = 5  # Assuming each team requires 5 players
        self.output_file = output_file

    def display_menu(self):
        menu_text = "Team Formation Tool POC Menu:\n" \
                "1. Create Player\n" \
                "2. Read Player\n" \
                "3. Update Player\n" \
                "4. Delete Player\n" \
                "5. Create Team\n" \
                "6. Create Team Rosters\n" \
                "7. Track Team Formation Changes\n" \
                "8. Exit\n"
        print(menu_text)  # Print menu text to console
#         self.write_to_file(menu_text)  # Write menu text to file

        


    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_player()
            elif choice == '2':
                self.read_player()
            elif choice == '3':
                self.update_player()
            elif choice == '4':
                self.delete_player()
            elif choice == '5':
                self.create_team()
            elif choice == '6':
                self.create_team_rosters()
            elif choice == '7':
                change_data = input("Enter change data: ")
                self.track_team_formation_changes(change_data)
            elif choice == '8':
                self.write_to_file("Exiting...\n")
                break
            else:
                self.write_to_file("Invalid choice. Please choose a valid option.\n")

    def write_to_file(self, text):
        with open(self.output_file, 'a') as file:
            file.write(text)

    def create_player(self):
        try:
            player_id = int(input("Enter Player ID: "))
            team_id = int(input("Enter Team ID: "))
            name = input("Enter Player Name: ")
            skills = input("Enter Player Skills: ")
            self.player_db.create_player(player_id, name, skills)
            self.write_to_file("Player created successfully.\n")
        except ValueError as e:
            self.write_to_file("Error: {}\n".format(e))

    def read_player(self):
        try:
            player_id = int(input("Enter Player ID: "))
            player = self.player_db.read_player(player_id)
            self.write_to_file("Player ID: {}\nName: {}\nSkills: {}\n".format(player.player_id, player.name, player.skills))
        except ValueError as e:
            self.write_to_file("Error: {}\n".format(e))

    def update_player(self):
        try:
            player_id = int(input("Enter Player ID: "))
            name = input("Enter new Name (press Enter to skip): ")
            skills = input("Enter new Skills (press Enter to skip): ")
            self.player_db.update_player(player_id, name, skills)
            self.write_to_file("Player updated successfully.\n")
        except ValueError as e:
            self.write_to_file("Error: {}\n".format(e))

    def delete_player(self):
        try:
            player_id = int(input("Enter Player ID: "))
            self.player_db.delete_player(player_id)
            self.write_to_file("Player deleted successfully.\n")
        except ValueError as e:
            self.write_to_file("Error: {}\n".format(e))

    def create_team(self):
        try:
            team_id = int(input("Enter Team ID: "))
            name = input("Enter Team Name: ")
            self.team_db.create_team(team_id, name)
            self.write_to_file("Team created successfully.\n")
        except ValueError as e:
            self.write_to_file("Error: {}\n".format(e))

    def create_team_rosters(self):
        try:
            team_id = int(input("Enter Team ID: "))
            team = self.team_db.read_team(team_id)
            players = list(self.player_db.players.values())
            
            if len(players) < self.MAX_PLAYERS_PER_TEAM:
                self.write_to_file("Not enough players in the database to create a roster.\n")
                return

            team_roster = players[:self.MAX_PLAYERS_PER_TEAM]
            del players[:self.MAX_PLAYERS_PER_TEAM]

            for player in team_roster:
                self.write_to_file("Player {} added to Team {}\n".format(player.name, team.name))

            # Here, you can perform additional logic to handle team rosters
            # such as balancing skills and statistics

        except ValueError as e:
            self.write_to_file("Error: {}\n".format(e))

    def track_team_formation_changes(self, change_data):
        # Implementation for tracking changes and updates to team formations
        pass

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
