import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup
import requests

url = 'https://www.skysports.com/premier-league-table'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

league_table = soup.find('table', class_='standing-table__table callfn')

club_names = []
points = []

for team in league_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        pl_team = row.find('td', class_='standing-table__cell standing-table__cell--name').text.strip()
        pl_points = int(row.find_all('td', class_='standing-table__cell')[9].text)
        club_names.append(pl_team)
        points.append(pl_points)

# Define a custom color palette using seaborn
palette = sns.color_palette("husl", len(club_names))

# Create a bar chart with custom colors
plt.figure(figsize=(10, 6))
bars = plt.barh(club_names, points, color=palette)
plt.xlabel('Points')
plt.title('Premier League Table')

# Invert the y-axis to display the highest points at the top
plt.gca().invert_yaxis()

# Add color labels to the bars (optional)
for bar, color in zip(bars, palette):
    bar.set_color(color)

# Display the chart
plt.show()
