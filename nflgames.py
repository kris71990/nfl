# nflgames.py 
# gets nfl weekly matchups and enters them into spreadsheet along with
# team records from nflteams.py

import requests, bs4, openpyxl, os, sys, nflteams

# get team information from internet 
url = 'http://www.vegasinsider.com/nfl/odds/las-vegas/'
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
teams_html = soup.select('.tabletext')
teams_raw = []

for item in teams_html:
	team = item.getText()
	teams_raw.append(team)

# create the matchups from teams_raw list
matchups = []
matchup_num = 0
matchup_num_2 = matchup_num + 1
num_games = int(len(teams_raw) / 2)
dict = nflteams.team_records_dict 

for i in range(0, num_games):
	matchups.append(teams_raw[matchup_num] + ' ' + dict.get(teams_raw[matchup_num]) + \
	' at ' + teams_raw[matchup_num_2] + ' ' + dict.get(teams_raw[matchup_num_2]))
	matchup_num += 2
	matchup_num_2 += 2

# open spreadsheet and write info
def write_game_info():
	os.chdir('/Users/kris/Desktop')
	wb = openpyxl.load_workbook('2017picksxl.xlsx')
	sheet = wb.get_sheet_by_name('Sheet 1')

	#find spreadsheet start row and write game info to appropriate cells
	write_matchup_num = 0
	start_row = 0
	start_week = sys.argv[1]
	for cell in sheet.columns[0]:
		if cell.value == start_week:
			start_row += 2
			for row_num in range(start_row, len(matchups) + start_row):
				game = sheet.cell(row=row_num, column=1)
				game.value = matchups[write_matchup_num]
				write_matchup_num += 1
		else: 
			start_row += 1

	wb.save('2017picksxlnew.xlsx')

print(matchups)
write_game_info()


