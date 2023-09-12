import random

# Historical data (replace with your actual historical data)
team_names = [
    "Manchester City", "Tottenham Hotspur", "Liverpool", "West Ham United",
    "Arsenal", "Brighton and Hove Albion", "Crystal Palace", "Brentford",
    "Nottingham Forest", "Aston Villa", "Manchester United", "Chelsea",
    "Fulham", "Newcastle United", "Wolverhampton Wanderers", "Bournemouth",
    "Sheffield United", "Everton", "Luton Town", "Burnley"
]

team_points = [
    12, 10, 10, 10, 10, 9, 7, 6, 6, 6, 6, 4, 4, 3, 3, 2, 1, 1, 0, 0
]

# Simulate the remainder of the season
num_matches_to_simulate = 10  # Change this to the number of remaining matches

for _ in range(num_matches_to_simulate):
    home_team = random.choice(team_names)
    away_team = random.choice([team for team in team_names if team != home_team])
    home_score = random.randint(0, 5)  # Simulate scores
    away_score = random.randint(0, 5)

    # Update team points based on the simulated match
    home_team_index = team_names.index(home_team)
    away_team_index = team_names.index(away_team)

    if home_score > away_score:
        team_points[home_team_index] += 3
    elif home_score < away_score:
        team_points[away_team_index] += 3
    else:
        team_points[home_team_index] += 1
        team_points[away_team_index] += 1

# Sort teams by points to get the final standings
final_standings = sorted(zip(team_names, team_points), key=lambda x: x[1], reverse=True)

# Display the final standings
for rank, (team, points) in enumerate(final_standings, start=1):
    print(f"{rank}. {team}: {points} points")
