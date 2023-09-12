from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

url = 'https://www.skysports.com/premier-league-table'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

league_table = soup.find('table', class_='standing-table__table callfn')

team_data = {}  # Create a dictionary to store team data

for team in league_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        pl_team = row.find('td', class_='standing-table__cell standing-table__cell--name').text.strip()
        pl_points = int(row.find_all('td', class_='standing-table__cell')[9].text)
        team_data[pl_team] = pl_points  # Store team name and points in the dictionary

# Sort the dictionary by points in descending order
sorted_team_data = dict(sorted(team_data.items(), key=lambda item: item[1], reverse=True))

# Extract team names and points to create the pie chart
team_names = list(sorted_team_data.keys())
team_points = list(sorted_team_data.values())

# Plot the pie chart
plt.figure(figsize=(10, 6))
plt.pie(team_points, labels=team_names, autopct='%1.1f%%', startangle=140)
plt.title('Premier League Standings (Pie Chart)')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Create a legend (key) for the pie chart
legend_labels = [f'{name} ({points} pts)' for name, points in zip(team_names, team_points)]
plt.legend(legend_labels, loc='best')

plt.show()
