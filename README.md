<h1 align="center">
  <br>
  Scraping NBA G League Players Data
  <br>
  <br>
</h1>

<h2 align="center">
  <br>
  Tugas 1 Seleksi Calon Warga Basdat 2021
  <br>
  <br>
</h2>

![Logo GLeague](https://media-exp1.licdn.com/dms/image/C511BAQGGtV05zbTaXg/company-background_10000/0/1519806642685?e=1627225200&v=beta&t=c1ZXNVgxmEz_crChO3kH3POzVPAHY_uQBdYC-6WRUhs)

## Table of Contents

This README.md contains the following
1. [Description](#description)
2. [Specification](#specification)
3. [How to use](#how-to-use)
4. [JSON Structure](#json-structure)
5. [Screenshots](#screenshots)
6. [Reference](#reference)
7. [Author](#author)


## Description

The NBA G League, or simply the G League, is the National Basketball Association's (NBA) official minor league basketball organization. The league was known as the National Basketball Development League (NBDL) from 2001 to 2005, and the NBA Development League (NBA D-League) from 2005 until 2017. As of the 2020–21 season, the league consists of 29 teams, 28 of which are either single-affiliated or owned by an NBA team, along with the NBA G League Ignite exhibition team. Their database contains players, teams, standings, and fixtures of the league.

In this project, the author made a program that scrape the players' data consists of their names, positions of playing, heights, weights, dates of birth, colleges, nationalities, and playing statistics per game provided by [this](https://gleague.nba.com/all-players/) webpage.

The database that is used to store the scraping results is PostgreSQL. PostgreSQL has earned a strong reputation for its proven architecture, reliability, data integrity, robust feature set, extensibility, and the dedication of the open source community behind the software to consistently deliver performant and innovative solutions. PostgreSQL also runs on all major operating systems.

## Specification

This program uses Javascript programming language and Node.js as the runtime environment. To run the program, you have to make sure you have installed Node.js and Postman to run the requests. You can install Node.js from [here](https://nodejs.org/en/) and Postman from [here](https://www.postman.com). You can also use other tools besides Postman to run requests. You can access the Postman Collections for this program [here](https://www.getpostman.com/collections/11f5a278dbda5e3eaae1).

## How to use

1. Make sure you already install Node.js.
1. Clone or download this repo to your local directory. 
2. Open the directory where you saved this repo and navigate to `src`.
3. Open the Terminal (for MacOS and Linux users) or Command Prompt (for Windows users) and run `npm install` to install all the dependecies needed.
4. Make sure you have a stable internet connection before running the code. This will avoid errors when running the code and speed up the process. 
5. Run `npm start` to start the server.
6. Open your web browser and go to `http://localhost:5000/`. Check that your browser will show up a HTML page that says `Hello, this is an NBA G League Players scraper!`. This is necessary to check whether the application is already running or not.
7. Run `http://localhost:5000/scrap-players` in your browser.  Wait for the response to come out.
8. Or you can open Postman and open the Postman collections to make it easier for you. Open the folder `Scraping [LOCAL]` and run the request. Wait for the response to come out.
9. After the response comes out, you can see the scraping data in JSON format in the response body. In addition, the resulting data is also generated in a JSON file located in the `Data Scraping/src/files` directory.

## JSON Structure

The scraped data will be converted into JSON format. Below is an example of the scraped data stored in JSON format.

<pre>
{
        "id": "1629824",
        "name": "Jalen Adams",
        "position": "Guard",
        "height": 188,
        "weight": 88,
        "dateOfBirth": "1995-12-11T00:00:00.000Z",
        "college": "Connecticut",
        "nationality": "USA",
        "ppg": 18.2,
        "rpg": 4.2,
        "apg": 4.6,
        "bpg": 0.39,
        "spg": 1.22,
        "mpg": 32.1
}
</pre>

## API
An online API has been provided to access this web scraping database. You can access it [here](https://pacific-chamber-65189.herokuapp.com). You can also download the Postman Collections [here](https://www.getpostman.com/collections/11f5a278dbda5e3eaae1).

## Screenshots
- Data Scraping Result

![Screenshot Scraping](https://raw.githubusercontent.com/andresjerriels/Seleksi-2021-Tugas-1/main/Data%20Scraping/screenshot/scrape.png)
- Data Storing in PostgreSQL
![Screenshot Storing](https://raw.githubusercontent.com/andresjerriels/Seleksi-2021-Tugas-1/main/Data%20Storing/screenshot/data.png)

## Reference
Libraries: 
- Puppeteer
- Cheerio
- Express
- node-postgres
- Bluebird
- Moment

## Author

Andres Jerriel Sinabutar
<br>
Informatics Engineering 
<br>
Institut Teknologi Bandung
