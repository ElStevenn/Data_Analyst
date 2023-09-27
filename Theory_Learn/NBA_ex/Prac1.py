import numpy as np
import pandas as pd




"""Data Loading and Initial Inspection""" 
DF = pd.read_csv("nba_data_processed.csv")
DF.fillna("")
# print(DF.head(10))
# print(DF.describe())


"""Data Filtering and Sorting"""
# Players who has played fewer than 20 games
PL_fw_20 = DF[DF["G"] < 20]
# print("Players played fewer than 20 games: ",PL_fw_20.shape[0])

# Sort players by their 'pts'
Sort_players = DF.sort_values(by="PTS", ascending=False)
# print(Sort_players)

"""Age Analysis"""
# FInd avarage age of the players
Average_age = DF["Age"].mean()
# print(Average_age)

# Find the youngests and oldests in the dataset:
Find_youngests = DF[DF["Age"] == DF["Age"].min()]
# print(Find_youngests)
Find_oldest = DF[DF["Age"] == DF["Age"].max()]
# print(Find_oldest)

"""Team Analysis"""
# Witch team has the most players in the dataset:
Team_order = DF.groupby(by="Tm").size()
# print(Team_order, "As we see, TOT team is the most players its team")

# Find the average age of the players of each team
team_list = DF["Tm"].unique().tolist()
result_avg = []
# print(team_list)
"""
for team in team_list:
    select_team = DF[DF["Tm"] == team]
    avg_age = select_team["Age"].mean()
    print(f"Average age for team {team}: {avg_age:.2f}")
    result_avg.append(avg_age)"""


"""INTERMEDIATE EXERCISES """

"""Shooting Proficiency"""
# Calculation the average FG%, 3P%, and FT% across all players.
FG_average = DF["FG%"].mean()
_3P_average = DF["3P%"].mean()
FT_average = DF["FT%"].mean()

# print(FG_average)
# print(_3P_average)
# print(FT_average)

# Identify players who have above average in all three percentages.

above_average_players = DF[(DF["FG%"] > FG_average) &
                            (DF["3P%"] > _3P_average) &
                            (DF["FT%"] > FT_average)]

# print(above_average_players.shape)

"""Rebound Analysis"""
# Which player has the highest total rebounds (TRB) per game played (G)?
DF['TRB_per_game'] = DF['TRB'] / DF['G']

top_rebounder = DF[DF['TRB_per_game'] == DF['TRB_per_game'].max()]
# print(top_rebounder[["Player", "TRB_per_game"]])

"""Assist to Turnover Ratio"""
# Calculate the assist to turnover ratio (AST/TOV) for each player.
# DF['AST_TOV_ratio'] = DF["AST"] / DF["TOV"]
DF['AST_TOV_ratio'] = np.where(DF['TOV'] != 0, DF['AST'] / DF['TOV'], np.nan)

# print(DF[['Player', 'AST_TOV_ratio']])

# Find the top 5 players with the highest ratio
Top_5_h_r = DF.sort_values(by="AST_TOV_ratio" ,ascending=False).head(5)
# print(Top_5_h_r[["Player","AST_TOV_ratio"]])

"""Positional Analysis"""
# group the dataset by position (Pos). For each position, calculate the average PTS, AST, and REB.
position_averages =  DF.groupby('Pos')[['PTS', 'AST', 'TRB']].mean()
# print(position_averages)

"""Efficiency Analysis"""

# Find the top 5 players with the highest eFG%.
Top_5_hig_efg = DF["eFG%"].max()
# print(Top_5_h_r)

"""Defensive Abilities"""
# Calculate a "Defensive Score" for each player using the formula: DScore = (DRB + (2 * STL) + (3 * BLK)) / G. 
# Find the top 5 players based on this score

DF["Defensive_Score"] = (DF['DRB'] + (2 * DF['STL']) + (3 * DF['BLK'])) / DF['G']
Top_5_DefenScor = DF.sort_values(by="Defensive_Score", ascending=False).head(5)
# print(Top_5_DefenScor)

"""Advanced Exercises"""
"""Correlation Analysis"""
# Using Numpy or Pandas, find out which pair of the following metrics have the 
# strongest positive correlation: PTS, AST, TRB, TOV.

