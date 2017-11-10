# byeteams.py
# accesses weekly schedule and identifies bye teams

import requests, bs4, sys

week_num = sys.argv[1]
    
if isinstance(week_num, str):
    week_num = week_num.split(' ')
    week_num = week_num[1]

url = 'http://www.espn.com/nfl/schedule/_/week/' + week_num
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
bye_teams_html = soup.select('.odd.byeweek a span')
bye_teams = []

def get_bye_teams():
    
	for each in bye_teams_html:
		team = each.getText()
		bye_teams.append(team)
	
	print("*Bye - ", end="")
	count = 0	
	for each in range(0, len(bye_teams)): 
		count += 1
		if count == len(bye_teams):
			print(bye_teams[each])	
		else:
			print(bye_teams[each] + ', ', end="")


