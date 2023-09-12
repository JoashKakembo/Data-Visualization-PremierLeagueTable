import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests

url = 'https://www.skysports.com/premier-league-table'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

league_table = soup.find('table', class_='standing-table__table callfn')

club_names = []
points = []

relegation_threshold = 3  # Define the threshold for relegation zone

for team in league_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        pl_team = row.find('td', class_='standing-table__cell standing-table__cell--name').text.strip()
        pl_points = int(row.find_all('td', class_='standing-table__cell')[9].text)
        club_names.append(pl_team)
        points.append(pl_points)

# Create a table-like structure
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('tight')
ax.axis('off')

# Create a table with headers and rows
table_data = [['Club', 'Points']]

for club, point in zip(club_names, points):
    if point <= relegation_threshold:
        # Highlight teams in the relegation zone with a different background color
        table_data.append([club, point])

table = ax.table(cellText=table_data, cellLoc='center', loc='center', colColours=['lightgray', 'lightgray'])

# Adjust the cell heights for better appearance
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1, 1.5)

# Set a title
plt.title('Premier League Club Points Distribution')

# Show the table
plt.show()
