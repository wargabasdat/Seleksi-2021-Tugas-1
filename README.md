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

## Deskripsi Data dan DBMS

Melakukan data scraping dari website pergikuliner.com. Data yang diambil berupa data 300 restoran di Jakarta (Nama, Alamat, Daerah, Tipe Kuliner, Kisaran Harga, Rating, Pembayaran, Cabang, dan Fasilitas). Data tersebut saya pilih karena banyak orang yang senang untuk mencari informasi tentang suatu restoran sebelum mengunjunginya.

Melakukan data storing dari file data.json ke DBMS MongoDB dan MongoDB Atlas. DBMS tersebut saya pilih karena beberapa alasan berikut:

1. File awal sudah dalam format json sehingga lebih mudah untuk import data ke database NoSQL.
2. Database NoSQL lebih memiliki struktur data yang lebih fleksibel untuk dimodifikasi.
3. MongoDB merupakan salah satu database NoSQL yang populer dan sering digunakan oleh banyak developer.

## Spesifikasi Program

Program menggunakan bahasa pemrograman Python dengan library BeautifulSoup, requests, json, time.

- Library BeautifulSoup digunakan untuk melakukan data scraping dari website dengan menggunakan fungsi find dan find_all.
- Library requests digunakan untuk mengirim request http ke suatu website.
- Library json digunakan untuk mengubah data menjadi file dengan format json.
- Library time digunakan untuk memberikan jeda waktu request data dari website dengan menggunakan fungsi sleep() untuk mencegah request data yang terlalu banyak.

## How to Use

### Data Scraping

1. Mendownload folder Data Scraping atau clone repository ini
2. Menginstall Python dan BeautifulSoup
3. Membuka file main.py
4. Mengganti variabel path sesuai direktori data.json pada laptop/komputer anda
5. Mengganti variabel from_page dan until_page menjadi halaman awal dan akhir yang ingin diambil datanya dari website
6. Menjalankan file main.py
7. Data akan langsung tersimpan pada file data.json dalam folder data.

### Data Storing

1. Mendownload folder Data Storing atau clone repository ini
2. Menginstall MongoDB
3. Membuka cmd dan cd ke direktori C:\Program Files\MongoDB\Server\4.4\bin (disesuaikan)
4. Meng-import data dari file data.json

```
mongoimport --jsonArray --db <nama database> --collection <nama collection> --file <direktori data.json>
```

5. Mengecek hasil import data

```
mongo
```

```
use <nama database>
```

```
db.<nama collection>.find().sort({id:1}).limit(10).pretty()
```

6. Meng-export data dari MongoDB

```
mongoexport --collection=<nama collection> --db=<nama database> --out=<nama file>
```

## JSON Structure

```
{
    "restaurants": [
        {
            "id": string,
            "nama": string,
            "alamat": string,
            "daerah": string,
            "tipe kuliner": array of string,
            "kisaran harga": string,
            "rating": float,
            "pembayaran": array of string,
            "cabang": boolean,
            "fasilitas": array of string
        },
        ..
    ]
}
```

## Screenshot Program dan Penjelasan

### Data Scraping

#### Data Sebelum Program Dijalankan

#### Program 1 Mengambil Data Restoran dari Page 1-10

#### Program 2 Mengambil Data Restoran dari Page 11-20

Program ini diulang sebanyak 3 kali karena ditemukan kesalahan saat pengambilan data.

#### Program 3 Mengambil Data Restoran dari Page 21-25

#### Data Setelah Program 1, 2, 3 Selesai Dijalankan

Setelah pengecekan ulang data json, ditemukan data yang duplikat karena program 2 diulang namun data yang sudah tersimpan belum dihapus sehingga total baris pada file json berbeda dengan hasil screenshot. Selain itu, nama atribut "harga" diubah menjadi "kisaran harga" agar tidak rancu.

#### Program 4 Mengambil Data Restoran dari Page 26-30

#### Program 5 Mengambil Data Restoran dari Page 31-40

#### Data Setelah Seluruh Program Selesai Dijalankan

### Data Storing

## References

Berikut daftar library yang digunakan beserta referensi lainnya:

1. BeautifulSoup

- https://pypi.org/project/beautifulsoup4/

2. requests

- https://pypi.org/project/requests/

3. json

- https://www.geeksforgeeks.org/append-to-json-file-using-python/

4. time

- https://docs.python.org/3/library/time.html

5. Referensi lainnya
   Website untuk scraping data:

- https://pergikuliner.com/restaurants?utf8=%E2%9C%93&search_place=&default_search=Jakarta&search_name_cuisine=&commit=

  Panduan data scraping:

- http://bit.ly/DataScrapingGuidance

  Link tutorial Youtube:

- https://www.youtube.com/watch?v=XVv6mJpFOb0&ab_channel=freeCodeCamp.org

Data Storing:

- https://docs.mongodb.com/v4.2/reference/program/mongoexport/
- https://www.youtube.com/watch?v=Phe9B2HRVmc&t=101s&ab_channel=PraveenKumar
- https://github.com/beaucarnes/mern-exercise-tracker-mongodb/tree/master/backend

## Author

Jacelyn Felisha
18219097
Sistem dan Teknologi Informasi ITB 2019
