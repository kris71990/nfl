# NFL Weekly Tracker

**Author: Kris**

**Version: 2.0.0**

## About

These files scrape weekly matchup data and scores from the weekly NFL schedule and enter the information into an Excel spreadsheet.

## Getting Started

These scripts use the following libraries:
> <a href="https://docs.python-requests.org/en/latest/user/install/#install">***requests***</a>
> for fetching data from the internet

> <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">***bs4***</a>
> for parsing html response data

> <a href="https://openpyxl.readthedocs.io/en/stable/">***openpyxl***</a>
> for editing excel spreadsheets


> <a href="https://pypi.org/project/python-dotenv/">***dotenv***</a>
> for enironment variables 


Create a .env file in root of project. The .env file must contain the following variables:
```
PATH={ Name of path }
EXCEL_FILE={ Name of excel file }
EXCEL_FILE_NEW={ Name of new excel file }
```

The `PATH` is the location on your computer from which to load and save the excel files. The `EXCEL FILE` is the name of an existing excel file that will be edited. `EXCEL_FILE_NEW` is the name of a new file that will be saved after editing.



### Documentation

`teaminfo.py` - a dictionary of team names and abbreviations, which is imported by `nflgames.py` and used throughout the app.

`nflteams.py` - scrapes <a href="http://www.vegasinsider.com/nfl/odds/las-vegas/">Vegas Insider</a> for weekly game matchup information and betting lines. This file is imported by `nflgames.py`.

`byeteams.py` - scrapes <a href="http://www.espn.com/nfl/schedule/">ESPN</a> to find the teams on bye during that week, if any. Imported by `nflgames.py`.

`nflgames.py` - Finds all matchup data for the upcoming week and enters it into an excel spreadsheet. For the data to be entered, there must be a cell in a column of the spreadsheet that says 'Week X', where X is the integer of the upcoming week.

`nflscores.py` - Records all scores from the previous week and enters them into the spreadsheet beside the matchup columns (entered by `nflgames.py`).

`tallyscores.py` - Analyzes scores and user picks and color codes cells depending on correct/incorrect picks. Is run when invoking `nflscores.py` (see above)

---

There are two actions to take.
1. Schedule

Ex. Running the following will enter the schedule and betting lines for Week 2:

     python nfl.py schedule 'Week 2'
     OR
     python nfl.py schedule 2

2. Scores

Ex. Running the following will enter the scores from Week 1:

     python nfl.py scores 'Week 1'
     OR
     python nfl.py scores 1

For best results dependent on how *Vegas Insider* is structured, the `Schedule` action should be run after the previous week is complete and before the next week begins (Tuesday or Wednesday on usual weeks). The `Scores` action should be run similarly - after all games have completed for the week and before the next week's games begin.


### Demo

<image src="assets/nfl-demo.png" width=600>

This is an example spreadsheet formatted for the application. 

Columns A and B are where matchups and betting lines are entered through the `Schedule` action. 

Column C is for final scores. Columns H-K are for user picks and are color coded depending on game results. This is accomplished with the `Scores` action.