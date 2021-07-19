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


### **Webscraping data pemain NBA**
Melakukan *data scraping* dari website NBA (https://www.nba.com/players), untuk medapatkan seluruh data pemain NBA saat ini dan menyimpannya pada sebuah *database*. **MongoDB** akan digunakan sebagai **DBMS**, karena *field* pada data tidak terlalu banyak sehingga tidak memerlukan skema relasional pada *database*, serta data hasil *data scraping* akan disimpan dalam format `JSON`, maka penggunaan **MongoDB** dapat membuat proses *import* data ke dalam *database* sebagai **DBMS** menjadi lebih efektif.  


### Data Scraping
### Spesifikasi
1. Source code *data scraping* menggunakan bahasa pemrograman`Python` 
2. Pada website (https://www.nba.com/players) terdapat tabel yang berisi data-data pemain NBA, dengan format tabel seperti gambar di bawah.
3. Diperlukan sebuah `webdriver` dalam proses *data scraping* untuk dapat melakukan navigasi otomatis pada halaman website. Pada source code ini saya menggunakan [Chrome Webdriver](https://chromedriver.chromium.org/downloads)


![](Data%20Scraping/screenshot/nba_com_players.jpg)

### How to Use
1. `Clone repository` ini
2. *Install* seluruh *library* dengan :

```
pip install -r requirements.txt
```
3. Buka `webscrap.ipynb` pada `Jupyter Notebook`
4. Jalankan program.



### JSON Structure
Berikut adalah struktur `json` dari data hasil *scraping*

```
{
    "name": string,
    "team": string,
    "number": integer,
    "position": string,
    "height": float,
    "weight": integer,
    "school": string,
    "country": string
}

```
Contoh data hasil *scraping* seperti berikut.
```
{
    "name": "Bam Adebayo",
    "team": "Miami Heat",
    "number": 13,
    "position": "C-F",
    "height": 210.3,
    "weight": 115,
    "school": "Kentucky",
    "country": "USA"
}
```

`notes : height dan weight sudah dalam satuan cm dan kg.`
`file NBAPlayers.json telah di-parse menggunakan extensions Prettier pada Visual Studio Code `

### Screenshot
- __*Scraping*__
![](/Data%20Scraping/screenshot/scraping_1.png)
![](/Data%20Scraping/screenshot/scraping_2.png)

- Dump data to json
![](/Data%20Scraping/screenshot/scraping_3.png)

### Data Storing

### Deskripsi
Data hasil *scraping* akan disimpan pada *database*. DBMS yang saya gunakan adalah __MongoDB__ (untuk *local* dbms) dan __MongoDB Atlas__ (untuk *cloud* dbms).



### Store data to local DBMS
Untuk menyimpan data pada *local*  dbms saya menggunakan __tool mongoimport__ dengan cara : 
- Membuka *directory* `NBAPlayers.json` pada terminal
- Lalu menjalankan command berikut
```
mongoimport --db NBA --collection NBAPlayers --file NBAPlayers.json --jsonArray

```
### Store data to cloud DBMS
Untuk menyimpan data pada *cloud* dbms, petama saya membuat *cluster* pada __MongoDB Atlas__, lalu saya juga menggunakan __tool mongoimport__ untuk meng-import file json ke *cloud* dbms dengan cara : 
- Membuka *directory* `NBAPlayers.json` pada terminal
- Lalu menjalankan command berikut
```
mongoimport --host learning-shard-00-02.xpygv.mongodb.net:27017 --db nba --type json --file NBAPlayers.json --jsonArray --authenticationDatabase admin --ssl --username admin --password admin

```


### Screenshot
- Local Data Storing
![](/Data%20Storing/screenshot/storingLocal_1.png)
![](/Data%20Storing/screenshot/storingLocal_2.png)
![](/Data%20Storing/screenshot/storingLocal_3.png)
![](/Data%20Storing/screenshot/storingLocal_4.png)
- Online/Cloud Data Storing
![](/Data%20Storing/screenshot/storingCloud_1.png)
![](/Data%20Storing/screenshot/storingCloud_2.png)

### API
Saya mambuat `API` sederhana untuk dapat mengakses *online database*, dan dapet melakukan operasi *create, read, update & delete (CRUD)*. `API` telah di-*deploy* pada tautan berikut. 
```
https://nba-players-api.herokuapp.com/players/

```

### How To Use API
1. Buka `Postman`
2. *Copy* tautan (https://nba-players-api.herokuapp.com/players/) pada `Postman`
3. Lakukan *request method* `GET, POST, PATCH, & DELETE` lalu tekan *Send*

Berikut adalah beberapa contoh *request* yang dapat dijalankan.
### Screenshot
- **GET Method**

*Get all players data*
![](/Api/screenshot/postman_1.png)
*Get player data by id*
![](/Api/screenshot/postman_9.png)

- **POST Method**

*Create new player data*
![](/Api/screenshot/postman_2.png)
![](/Api/screenshot/postman_3.png)
- **PATCH Method**

*Update specific player data*
![](/Api/screenshot/postman_4.png)
![](/Api/screenshot/postman_5.png)
- **DELETE Method**

*Delete specific player data*
![](/Api/screenshot/postman_6.png)
![](/Api/screenshot/postman_7.png)
![](/Api/screenshot/postman_8.png)


### Tools and References
- Beautifullsoup4
- Selenium
- MongoDB
- MongoDB Atlas
- Node JS
- Express JS
- Mongoose
- Postman


- Mongoose documentation (https://mongoosejs.com/docs/api.html)
- Express documentation (https://expressjs.com/en/api.html)
- MongoDB documentation (https://docs.mongodb.com/)
- Scraping with BeautifullSoup tutorial (https://www.youtube.com/watch?v=XQgXKtPSzUI)
- Scraping with Selenium tutorial (https://www.youtube.com/watch?v=Xjv1sY630Uc&t=558s)
- Rest API tutorial (https://www.youtube.com/watch?v=vjf774RKrLc)


### Author
```
M Rifandy Zulvan
Sistem dan Teknologi Informasi
18219021
```
