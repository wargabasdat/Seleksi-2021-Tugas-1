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


## Data & DBMS Description

### Data
This project scrapes listings from Airbnb's Unique Stays Collection

### DBMS
The DBMS used to store the data is MongoDB Atlas, MongoDB's cloud database. It's an Open-Core NoSQL Document Database which is suitable for semi-structured data like json. Cloud database is relatively safer and MongoDB is simple and free to use.


## Program Specification
Language: Python version 3.8

## How to Use


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


## Libraries
```
- requests (used to send http request)
- json (used to store json data after scraping)
- BeautifulSoup (used to scrape the data)
- pymongo (used to store the data into MongoDB Atlas)
```

## Author
Aisyah Farras Aqila

13519054


```
- Description of the data and DBMS (Why you choose it)
- Specification of the program
- How to use
- JSON Structure
- Screenshot program (di-upload pada folder screenshots, di-upload file image nya, dan ditampilkan di dalam README)
- Reference (Library used, etc)
- Author
```

