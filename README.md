<h1 align="center">
  <br>
  Real Estate in Indonesia
  <br>
  <br>
</h1>

<h2 align="center">
  <br>
  Data Scraping & Data Storing from rumah123.com
  <br>
  <br>
</h2>

![Logo Rumah123](/main/Data%20Scraping/screenshot/logo-rumah123.jpg?raw=true)

## Table of Contents

This README.md contains the following
1. [Description](#description)
2. [Specification]()
3. [How to use]()
4. [JSON Structure]()
5. [Screenshots]()
6. [Reference]()
7. [Author]()


## Description

Rumah123 is the main search engine on real estates and properties in Indonesia. Since 2007, they served millions of Indonesians to find properties and invest on real estates. With over 900.000 property listings, they have one of the largest and the most comprehensive database in Indonesia. Their database contains location, land area, building area, number of rooms and also prices of every property that we could think of.

The data collected by this web scraper contains the property listing title, property agent, location, phone number, property area, price, and number of rooms provided by http://rumah123.com/jual/rumah webpage

On this project, the author will be using MongoDB as the default DBMS because MongoDB offers high performance, easy, and a more flexible way to store data. MongoDB offers flexibility because it uses JSON document that can be modified independently without affecting the entire data structure.

## Specification

To run the program, we will need some library to make the program work

- #### Jupyter Notebook
To make the code easier to write and easier to maintain, the author chooses to use Jupyter Notebook for this project. All scripts will be stored in .ipynb format

To install, type
```
pip install notebook
```
on your terminal.

- #### BeautifulSoup

Because the author uses Python as the main programming language for this project, BeautifulSoup is an excellent tool to help the user scrapes website easily. The author chooses BeautifulSoup because this library is easy to understand and have a fairly simple syntax.

To install BeautifulSoup library, type
```
pip install beautifulsoup4
```
in your terminal.

- #### urllib3
Because we will grab HTML from rumah123 website, we need a library to help us grab the raw HTML of the website. The author chooses urllib3 because it is widely used in the community and has a great documentation.

To install, type
```
pip install urllib3
```
in your terminal.

- #### TQDM
Web scraping could take some time. If you're scraping hundreds of pages, we need a way to monitor our script's progress. TQDM is a great tool for this kind of problem, because TQDM will show us a progress bar on our loop (for loops, while loops) while scraping the website.

To install, type
```
pip install tqdm
```
in your terminal.


- #### Time
Most websites have anti-scraping mechanism if they sense unusual activities from certain users. To avoid it and to keep the server from crashing, we will put our program on sleep using the time.sleep() method. Time library is already preinstalled with Python.

- #### JSON
The scraped data will be stored in JSON format. To dump the scraped data into JSON format, we need the JSON library. JSON library is already preinstalled with Python

- #### Geopy
Because we have location info from the website, it is a great opportunity to also store the latitude and longitude of the location, so we can better visualize the data using the geographical data.

To install, type
```
pip install geopy
```
in your terminal


## How to use

1. Make sure you have already installed all the necessary libraries in this project. 

2. Make sure you have a stable internet connection before running the code. This will avoid errors when running the code. 

3. Clone this repository to your local directory.

Type
```
git clone https://github.com/tugusav/Seleksi-2021-Tugas-1.git
```
on your terminal

4. Open Jupyter Notebook by changing the directory on your terminal to the repository and typing
```
jupyter-notebook
```

5. Open webscraper.ipynb and run the code on Jupyter Notebook

6. Make sure to run 4 different web scraping intervals in different times to avoid anti-scraping mechanism on rumah123.com

## JSON Structure

The scraped data will be converted into JSON format. Below is an example of the scraped data stored in JSON format.

<pre>
{
        "property_title": "Rumah Mozart Golf Island PIK View Golf (10x30m)",
        "property_agent": "MR REALTY - GOLF ISLAND",
        "location": "Pantai Indah Kapuk, Jakarta Utara",
        "latitude": -6.1244359,
        "longitude": 106.7532766,
        "phone_number": "+628568888322",
        "property_type": "Rumah",
        "land_area": 300,
        "building_area": 400,
        "price_idr": 16000000000,
        "num_bathroom": 4,
        "num_bedroom": 4,
        "garage_capacity": 1
    },
</pre>

## Screenshots

- #### Scraping Function
![Scraper Function 1](/main/Data%20Scraping/screenshot/scraper-function1.png?raw=true)
![Scraper Function 2](/main/Data%20Scraping/screenshot/scraper-function2.png?raw=true)

- #### Progress Bar using TQDM
![Scraping with TQDM](/main/Data%20Scraping/screenshot/scraping-tqdm.png?raw=true)

- #### Preprocessing Input Data
![Preprocessing Input Data](/main/Data%20Scraping/screenshot/preprocessing-input.png?raw=true)

- #### Output to JSON
![Output to JSON](/main/Data%20Scraping/screenshot/concat-and-output-to-json.png?raw=true)

- #### Data Storing in MongoDB
![Data Storing MongoDB](/main/Data%20Scraping/screenshot/storing-mongo.png?raw=true)

## Reference

Web Scraping with Beautiful Soup Tutorial
- https://www.youtube.com/watch?v=XVv6mJpFOb0

For all libraries documentation, details can be found here
- https://pypi.org/

About how to avoid getting blocked while scraping websites
- https://www.codementor.io/@scrapingdog/10-tips-to-avoid-getting-blocked-while-scraping-websites-16papipe62

Resolving every error :D
- https://stackoverflow.com



## Author

Ida Bagus Raditya Avanindra Mahaputra
Information System and Technology (18219117)
Institut Teknologi Bandung