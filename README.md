# NFL Weekly Tracker

**Author: Kris**
**Version: 2.0.0**

## About

These files scrape weekly matchup data from the weekly NFL schedule and then enter the information into an Excel spreadsheet.

### Documentation

`teaminfo.py` - a dictionary of team names and abbreviations, which is imported by `nflgames.py`

`nflteams.py` - scrapes http://www.vegasinsider.com/nfl/odds/las-vegas/ for weekly game matchup information, which is imported by `nflgames.py`

`byeteams.py` - scrapes http://www.espn.com/nfl/schedule/_/week/[ integer number of current week ] to find the teams on bye during that week, if any. Imported by `nflgames.py`

`nflgames.py` - run `python3 nflgames.py 'Week [ integer number of current week ]'` in the command line to retrieve all matchup data. This data is then entered into an Excel spreadsheet.

