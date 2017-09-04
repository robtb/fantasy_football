import csv
from database import DatabaseInterface
import utilities as ut


players_dir_path = 'c:/my_projects/fantasy_football/players/'
db = 'c:/sqlite/chinook/sample.db'
dbi = DatabaseInterface(db)
# pos = 0, name = 2, fgm = 7, team = 12
def load_kickers(kickers_csv):
    """pos = 0, name = 2, fgm = 7, team = 12"""
    with open(players_dir_path + kickers_csv, 'r', newline='') as infile:
        kickers = csv.reader(infile)
        for kicker in kickers:
            if ut.input_is_integer(kicker[7]):
                score = ut.kicker_score(int(kicker[7]))
            else:
                score = 0
            dbi.add_player_to_game(kicker[2], kicker[0], kicker[12], score)


def load_quarterbacks(quarterbacks_csv):
    """IN the csv, pos is [0], name = [2], team = [12[, tds = [5], int = [7], yards= [9]"""
    with open(quarterbacks_csv, 'r', newline='') as infile:
        quarterbacks = csv.reader(infile)
        for quarterback in quarterbacks:
            if ut.input_is_integer(quarterback[5]):
                tds = int(quarterback[5])
            else:
                tds = 0
            if ut.input_is_integer(quarterback[7]):
                interceptions = int(quarterback[7])
            else:
                interceptions = 0
            # LOSE THE COMMSAS
            if ut.input_is_integer(quarterback[9].replace(',', '')):
                yards = int(quarterback[9].replace(',', ''))
            else:
                yards = 0
            dbi.add_player_to_game(quarterback[2], quarterback[0], quarterback[12], ut.quarterback_score(yards, tds,
                                                                                                        interceptions))


def load_runningbacks(runningbacks_csv):
    """yds at index 7 and tds 11"""
    with open(players_dir_path + runningbacks_csv, 'r', newline='') as infile:
        runningbacks = csv.reader(infile)
        for runningback in runningbacks:
            # yds may be over 1000, NFL.com formats using commas so they must be removed
            if ut.input_is_integer(runningback[7].replace(',', '')):
                yds = int(runningback[7].replace(',', ''))
            else:
                yds = 0
            if ut.input_is_integer(runningback[11]):
                tds = int(runningback[11])
            else:
                tds = 0
            dbi.add_player_to_game(runningback[2], runningback[0], runningback[12], ut.running_back_score(yds, tds))

def load_wide_receivers(receiver_csv):
    """Workds for tightends and wide receivers.  receptions [5], yards [7],  tds [11]"""
    with open(players_dir_path + receiver_csv, 'r', newline='') as infile:
        receivers = csv.reader(infile)
        for receiver in receivers:
            if ut.input_is_integer(receiver[5]):
                receptions = int(receiver[5])
            else:
                receptions = 0
            if ut.input_is_integer(receiver[7].replace(',', '')):
                yds = int(receiver[7].replace(',', ''))
            else:
                yds = 0
            if ut.input_is_integer(receiver[11]):
                tds = int(receiver[11])
            else:
                tds = 0
            dbi.add_player_to_game(receiver[2], receiver[0], receiver[12], ut.receiver_scoring(receptions, yds, tds))

load_wide_receivers('tightends.csv')
