import sqlite3


class DatabaseInterface:
    def __init__(self, database_path):
        """create connection and cursor when class is instantiated
        :rtype: object
        """
        self.conn = sqlite3.connect(database_path)
        self.cur = self.conn.cursor()

    def add_user(self, user_name, team_name):
        """creates a new orphan user in system with no league id assigned.  INTEGER PRIMARY KEY is auto assigned"""
        action = "INSERT INTO users (user_name, team_name VALUES (?, ?)"
        data = (user_name, team_name)
        self.cur.execute(action, data)
        self.conn.commit()
        return self.cur

    def assign_user_to_league(self, user_id, league_id):
        """assigns a league_id to a user which is a foreign key"""
        action = "UPDATE users SET league_id=? WHERE user_id=?"
        data = (league_id, user_id)
        self.cur.execute(action, data)
        self.conn.commit()
        return self.cur

    def add_player_to_game(self, player_name, position, team, last_year_score):
        """this function is only called  during initial set up of game, populates the player db with players.  INTEGER
        PRIMARY KEY is auto assigned"""
        action = "INSERT INTO players (name, team, lastyearscore, position) VALUES(?, ?, ?, ?)"
        data = (player_name, team, last_year_score, position)
        self.cur.execute(action, data)
        self.conn.commit()
        return self.cur

    def get_lastyear_stats(self, position):
        action = "SELECT name, ROUND(lastyearscore, 2) FROM players WHERE position = ? ORDER BY lastyearscore DESC;"
        data = (position,)
        self.cur.execute(action, data)
        return self.cur

    def __del__(self):
        """destroys instance and connection on completion of called method"""
        self.conn.close()
