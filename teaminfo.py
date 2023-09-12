import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import mplcursors  # Import mplcursors

url = 'https://www.skysports.com/premier-league-table'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

league_table = soup.find('table', class_='standing-table__table callfn')

club_names = []
points = []
team_info = []  # Store team information for annotations

for team in league_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        pl_team = row.find('td', class_='standing-table__cell standing-table__cell--name').text.strip()
        pl_points = int(row.find_all('td', class_='standing-table__cell')[9].text)
        club_names.append(pl_team)
        points.append(pl_points)
        # Collect team information for annotations
        team_info.append(f'{pl_team}: {pl_points} points')

# Create a bar chart
plt.figure(figsize=(10, 6))
bars = plt.barh(club_names, points, color='skyblue')
plt.xlabel('Points')
plt.title('Premier League Table')

# Invert the y-axis to display the highest points at the top
plt.gca().invert_yaxis()

# Add annotations when hovering over bars
cursor = mplcursors.cursor(hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(team_info[sel.target.index]))

# Display the chart
plt.show()
