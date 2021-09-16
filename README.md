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

Running the following will collect and enter matchup data for Week 2:

    python3 nflgames.py 'Week 2'
    OR
    python3 nflgames.py 2

For best results dependent on how *Vegas Insider* is structured, this command should be run after Week 1 is complete and before Week 2 begins (Tuesday or Wednesday on usual weeks).


`nflscores.py` - Records all scores from the previous week and enters them into the spreadsheet beside the matchup columns (entered by `nflgames.py`).

Running the following will enter the scores from Week 1:

     python3 nflscores.py 'Week 1'
     OR
     python3 nflscores.py 1


### Demo
