
# Use the bullet module, so that user can select 'team' from a list.


import pandas as pd
import numpy as np

df1 = pd.read_csv('clean_bundesliga_data.csv')

# Create a list of all the teams that a user can choose from.

def get_team():
    global team
    team = input("What team do you want to see statistics for?\n")
#    if team.title() not in teams:
#        team = input("We only have data for Bundesliga teams. Pick one.")

    print('-'*40)
    return team

def game_stats(team):

    # How many games the team played
    away_count = df1.query('away_team == "%s"' % team).away_team.count()
    home_count = df1.query('home_team == "%s"' % team).away_team.count()
    games_played = away_count + home_count

    # How many games the team won
    games_won = df1.query('result == "%s"' % team).result.count()

    # How many games the team drew
    home_games_drawn = df1.query('result == "Draw" and home_team == "%s"' % team).result.count()
    away_games_drawn = df1.query('result == "Draw" and away_team == "%s"' % team).result.count()
    games_drawn = home_games_drawn + away_games_drawn

    # How many games the team lost
    games_lost = games_played - (games_won + games_drawn)

    # Print results
    print(team, "Game Statistics, 2008-2016")
    print("Games played:", games_played)
    print("Games won:", games_won)
    print("Games lost:", games_lost)
    print("Games drawn:", games_drawn)


# Functions to call

def main():
    while True:
        get_team()
        game_stats(team)

        restart = input('\nWould you like to restart the program? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
