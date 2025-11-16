import numpy as np
import pandas as pd

# print("Jai Shree Ram")


df = pd.read_csv("ipl-matches.csv")

# df.info()

def Teams():
    teams = list(set((list(df['Team1']) + list(df['Team2']))))
    team_dict = {
        'teams': teams
    }

    return team_dict

def Team_Data(team):
    valid_teams = list(set(list(df['Team1']) + list(df['Team2'])))

    if team in valid_teams: 
        team_df = df[(df["Team1"] == team) | (df["Team2"] == team)]

        total_matches = team_df.shape[0]

        total_successful_matches = team_df["WinningTeam"].notna().sum()

        abandoned_matches = total_matches - total_successful_matches

        # Only matches of this team where they won
        matches_won = (team_df["WinningTeam"] == team).sum()

        # Completed matches (with winner)
        matches_lost = total_successful_matches - matches_won

        win_percent = int(((matches_won)/(total_successful_matches))*100)

        Team_data_dict = {
            "Total Matches": total_matches,
            "Matches Won": matches_won,
            "Matches Lost": matches_lost,
            "No Results": abandoned_matches,
            "Win Percentage" : win_percent
        }

        return Team_data_dict

    return {"error": "Team not found"}

def TeamVTeam(team1, team2):
    
    # All matches where both teams met
    newdf = df[
        ((df['Team1'] == team1) | (df['Team2'] == team1)) &
        ((df['Team1'] == team2) | (df['Team2'] == team2))
    ]

    Total_Matches = newdf.shape[0]

    Team1_Won = newdf[newdf["WinningTeam"] == team1].shape[0]
    Team2_Won = newdf[newdf["WinningTeam"] == team2].shape[0]

    draw = Total_Matches - (Team1_Won + Team2_Won)

    # Handle division by zero (if no match had a winner)
    if (Team1_Won + Team2_Won) == 0:
        Win_Percent_of_Team1 = 0
        Win_Percent_of_Team2 = 0
    else:
        Win_Percent_of_Team1 = (Team1_Won / (Team1_Won + Team2_Won)) * 100
        Win_Percent_of_Team2 = (Team2_Won / (Team1_Won + Team2_Won)) * 100

    TeamVTeam_Data = {
        "Total Matches": Total_Matches,
        "Team 1": team1,
        "Team 2": team2,
        "Team1 Won": Team1_Won,
        "Team2 Won": Team2_Won,
        "Draw / No Result": draw,
        "Win % of Team1": round(Win_Percent_of_Team1, 2),
        "Win % of Team2": round(Win_Percent_of_Team2, 2)
    }

    return TeamVTeam_Data

def Team_Players(team):

    newdf = df[(df["Team1"] == team) | (df["Team2"] == team)]

    players = []

    for _, row in newdf.iterrows():

        # TEAM 1
        if row["Team1"] == team:
            p = row["Team1Players"]
            if isinstance(p, list):
                players.extend(p)
            else:
                players.extend(p.split(","))

        # TEAM 2
        if row["Team2"] == team:
            p = row["Team2Players"]
            if isinstance(p, list):
                players.extend(p)
            else:
                players.extend(p.split(","))

    # Clean names + remove [] from name
    cleaned_players = []
    for p in players:
        p = p.strip()              # remove spaces
        p = p.replace("[", "")     # remove [
        p = p.replace("]", "")     # remove ]
        cleaned_players.append(p)

    unique_players = sorted(set(cleaned_players))

    return {
        "Team": team,
        "Total Unique Players": len(unique_players),
        "Players": unique_players
    }

