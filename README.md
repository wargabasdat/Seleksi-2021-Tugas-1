<h1 align="center">
  <br>
  Tugas 1 : Data Scraping & Data Storing
  <br>
  <br>
</h1>

<h2 align="center">
  <br>
  Steam Scrape
  <br>
  <br>
</h2>

## Specification of Program
Steam Scraper is a program that lets you scrape various data from steam listings. It includes listings like games, software, downloadable content, demos, and mods but it doesn't include things like soundtracks, videos, hardware, and inlcude bundles.

Beside scraping the data from Steam web, the program also facilitates/allows users to convert and store those data into a database (.sql file). Storing the data into a database form gives you freedom and flexibility on how you can utilize the data. For example, you can sort the listings by which app that has the biggest discount so you know what apps that offer the best fot their money,  you can listings with a particular review with certain percentage that builds the review itself, etc

All scripts in this repository are based on python languange with the integration of mariaDB DBMS for it in order to achieve all the database integration functions

## Description of the Data and DBMS
Data that are scraped include game title, release date of a game, original price and final price after all discounts are applied, game rating, percentage that builds the rating, total review from all users, game compatibility for each platform (Windows , Mac, Linux, VR compatible, VR only. These data were chosen because they can can be very helpful for users with their buying decision. E.g pricing, discount, review, etc. Hence why the program doesn't scrap listings like soundtracks, videos, hardware, and inlcude bundles because they don't represent the data that we're trying to look for.

For data storing purpose, mariaDB is choosen because it's basically an open source version of MySQL. It's developed to be as compatible with MySQL as possible. mariaDB offers some advantages : 
  - Because it's open source, it has wide variety of support and wide compatibility. This results in fast migration from one system to others. Plus there is a handful of documentations availabe on internet
  - Easy integration with python and that leads to ease when inserting all the data by using a python script
  - It's efficient and has better performance (Compared to MySQL). This is because of the large selection of alternative database engines.


## Requirements
In order to run the program, it requires the following programs/modules/packages to be installed
1. Python, tested using version 3.9.5
2. beautifulsoup4 python package
    `pip install beautifulsoup4`
3. A parser module package. There are a couple of options like 'lxml', 'html.parser', or 'html5lib' but I personally used 'html5lib'
    To install 'lxml' parser package
        `pip install lxml`
    To install 'hmtl.parser' parser package
        `pip install html-parser` or
        `pip install html.parser`
    To install 'html5lib' parser package
        `pip intall html5lib`
4. A DBMS, mariaDB
5. A python module package for connecting to mariaDB database
    `pip install mariaDB`

## How to use 
### Data scraping
All the scripts are basically normal python script, so you can run it however you want. The followings are how to run the python script on command prompt on Windows 10
1. Assuming you're on the main directory (Steam Scraper), change the directory to `Data Scraping/src`
    `cd Data Scraping/src`
2. Run the python script, `SteamScraper.py`
    `python SteamScraper.py` 
3. Wait for the process to be done and all the data that's been successfully scraped will be stored in data folder in JSON format

### Data Storing
First and foremost, I already made some scripts that'll automatically do all the queries in order to set up the database from creating the database and creating all the tables needed but if you want to do all the queries manually, I also make a text file that contains all the queries
1. Creating the database and all the tables
    First method, run an automcatic python script. Assuming you're still in Data Scraping/src directory
        `python SettingUpDatabase.py`
    Second method. If you want to setting up the database manually, you can run all the queries manually that you can check in a text file 
        SQL Query for Setting up Database.txt
2. Filling up the database with data
    To do this, all you have to do is to run a python script that I already made. This script will read JSON Files that were already made and then store it to database, steamscrape
        `python FillingDatabase.py`
3. After all the process is done, you should see a dump database file, steamscrape.py and a database, steamscrape in your system    


JSON Structure
There are 2 JSON Files as a result of the scraping process `SteamGame.json` and `SteamGenreDeveloper.json`
1. SteamGame.json
SteamGame.json contains all the data that are associated with game information with the structure as follows
```
{
  "GamesData": [
        {
            'game_title': gameTitle,
            'release_date': releaseDate,
            'original_price': originalPrice,
            'disc_price' : discPrice,
            'gaming_rating' : gamingRatingConc,
            'game_rating_percentage' : gameRatingPercentage,
            'total_user_reviews' : totalUserReviews,
            'win_compatibility' : winCompatibility,
            'mac_compatibility' : macCompatibility,
            'linux_compatibility' : linuxCompatibility,
            'vr_compatibility' : vrCompatibility,
            'vr_only' : vrOnly,
            'game_URL' : gameURL,
            'game_genres' : [gameGenres],
            'game_developer' : gameDeveloper
        },
        ......
        ......
        {
            'game_title': gameTitle,
            'release_date': releaseDate,
            'original_price': originalPrice,
            'disc_price' : discPrice,
            'gaming_rating' : gamingRatingConc,
            'game_rating_percentage' : gameRatingPercentage,
            'total_user_reviews' : totalUserReviews,
            'win_compatibility' : winCompatibility,
            'mac_compatibility' : macCompatibility,
            'linux_compatibility' : linuxCompatibility,
            'vr_compatibility' : vrCompatibility,
            'vr_only' : vrOnly,
            'game_URL' : gameURL,
            'game_genres' : [gameGenres],
            'game_developer' : [gameDeveloper]
        }
    ]   
}
```
2. SteamGenreDeveloper.json
SteamGenreDeveloper.json contains all the data that are associated with game genre and developers with the structure as follows
```
{
    "GenreData" : [genreList],
    "DeveloperData" : [gameDevList]
}
```

## Screenshot program 


## Reference
[Python Tutorial: Web Scraping with BeautifulSoup and Requests]
(https://www.youtube.com/watch?v=ng2o98k983k)

[Python Tutorial: Working with JSON Data using the json Module]
(https://www.youtube.com/watch?v=9N6a-VLBa2I)

[How to connect Python programs to MariaDB]
(https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/)


## Author
Mohammad Yahya Ibrahim
13519091