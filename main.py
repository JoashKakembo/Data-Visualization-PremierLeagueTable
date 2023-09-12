from bs4 import BeautifulSoup
import requests

url = 'https://www.skysports.com/premier-league-table'

r = requests.get(url)
# print(r)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup)


league_table = soup.find('table', class_ ='standing-table__table callfn')
# print(league_table)

for team in league_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        # pl_team  = row.find('td' , class_ = 'standing-table__cell standing-table__cell--name')
        # print(pl_team)
        
        pl_team  = row.find('td' , class_ = 'standing-table__cell standing-table__cell--name').text.strip()
        pl_points = row.find_all('td', class_ = 'standing-table__cell')[9].text 
        print(pl_team, pl_points)
        
        
        

 
