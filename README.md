<h1 align="center">
  <br>
  Seleksi Warga Basdat 2021
  <br>
  <br>
</h1>

<h2 align="center">
  <br>
  Tugas 1 : Data Scraping & Data Storing
  <br>
  <br>
</h2>

## Data
The data are listings from Airbnb's Unique Stays Collection.

## DBMS
The DBMS used to store the data is MongoDB Atlas, MongoDB's cloud database. It's an Open-Core NoSQL Document Database which is suitable for semi-structured data such as json. Cloud database is relatively safer and MongoDB is simple and free to use.

## Program Specification
Language: Python version 3.8

## Configuration
1. Add IP Address to IP Access List in MongoDB Atlas (can only be done by the author of this code).
2. Create ```config.py``` in ```src``` to store database's password in ```db_pass``` variable.

## How to Use
1. Set up configurations.
2. Open terminal.
3. Go to ```Data Scraping/src``` directory.
4. Run program with ```python3 scrape.py``` command.

## JSON Structure
```
_id     : Listing's id (_id is set as the default primary key in MongoDB)
type    : Type of the listing
area    : Where the listing is located
name    : Title of the listing
guest   : Number of guests
bedroom : Number of bedrooms
bed     : Number of beds
bath    : Number of baths
price   : Price per night in US Dollars
rating  : Listing's rating (set to 0 when not provided)
link    : Link to listing's page
```

## Program Screenshot
![picture alt](./Data%20Scraping/screenshot/program.png)

![picture alt](./Data%20Storing/screenshot/mongodb.png)

## Library
- requests (used to send http request)
- json (used to store json data after scraping)
- BeautifulSoup (used to scrape the data)
- pymongo (used to store the data into MongoDB Atlas)

## Author
Aisyah Farras Aqila - 13519054