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

Melakukan data scraping dari website **pergikuliner.com**. Data yang diambil berupa data __480 restoran di Jakarta__ (Nama, Alamat, Daerah, Tipe Kuliner, Kisaran Harga, Rating, Pembayaran, Cabang, dan Fasilitas). Data tersebut saya pilih karena banyak orang yang senang untuk mencari informasi tentang suatu restoran sebelum mengunjunginya.

Melakukan data storing dari file _`data.json`_ ke DBMS **MongoDB** dan **MongoDB Atlas**. DBMS tersebut saya pilih karena beberapa alasan berikut:

1. File awal sudah dalam format json sehingga lebih mudah untuk import data ke database NoSQL.
2. Database NoSQL memiliki struktur data yang lebih fleksibel untuk dimodifikasi.
3. MongoDB merupakan salah satu database NoSQL yang populer dan sering digunakan oleh banyak developer.

## Spesifikasi Program

Program menggunakan bahasa pemrograman Python dengan library BeautifulSoup, requests, json, time.

- Library **BeautifulSoup** digunakan untuk melakukan data scraping dari website dengan menggunakan fungsi _find()_ dan _find_all()_.
```
pip install beautifulsoup4
```
- Library **requests** digunakan untuk mengirim request http ke suatu website.
- Library **json** digunakan untuk mengubah data menjadi file dengan format json.
- Library **time** digunakan untuk memberikan jeda waktu request data dari website dengan menggunakan fungsi _sleep()_ untuk mencegah request data yang terlalu banyak.

## How to Use

### Data Scraping

1. Mendownload folder _`Data Scraping`_ atau clone repository ini
2. Menginstall Python dan BeautifulSoup
3. Membuka file _`main.py`_
4. Mengganti variabel **path** sesuai direktori _`data.json`_ pada laptop/komputer anda
5. Mengganti variabel **from_page** dan **until_page** menjadi halaman awal dan akhir yang ingin diambil datanya dari website
6. Menjalankan file _`main.py`_
7. Data akan langsung tersimpan pada file _`data.json`_ dalam folder _`data`_.

### Data Storing

1. Mendownload folder _`Data Storing`_ atau clone repository ini
2. Menginstall MongoDB
3. Membuka cmd dan cd ke direktori _`C:\Program Files\MongoDB\Server\4.4\bin`_ (disesuaikan)
4. Meng-import data dari file _`data.json`_

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

<img src="https://github.com/roscellyn/Seleksi-2021-Tugas-1/blob/main/Data%20Scraping/screenshot/data-before.png" width="50%">

#### Program 1 Mengambil Data Restoran dari Page 1-10

<img src="https://github.com/roscellyn/Seleksi-2021-Tugas-1/blob/main/Data%20Scraping/screenshot/program-1.png" width="50%">

#### Program 2 Mengambil Data Restoran dari Page 11-20

<img src="https://github.com/roscellyn/Seleksi-2021-Tugas-1/blob/main/Data%20Scraping/screenshot/program-2.png" width="50%">

Program ini diulang sebanyak 3 kali karena ditemukan kesalahan saat pengambilan data.

#### Program 3 Mengambil Data Restoran dari Page 21-25

<img src="https://github.com/roscellyn/Seleksi-2021-Tugas-1/blob/main/Data%20Scraping/screenshot/program-3.png" width="50%">

#### Data Setelah Program 1, 2, 3 Selesai Dijalankan

<img src="https://github.com/roscellyn/Seleksi-2021-Tugas-1/blob/main/Data%20Scraping/screenshot/data-mid.png" width="50%">

Setelah pengecekan ulang data json, ditemukan data yang duplikat karena program 2 diulang namun data yang sudah tersimpan belum dihapus sehingga total baris pada file json berbeda dengan hasil screenshot. Selain itu, nama atribut **harga** diubah menjadi **kisaran harga** agar tidak rancu.

#### Program 4 Mengambil Data Restoran dari Page 26-30

<img src="https://github.com/roscellyn/Seleksi-2021-Tugas-1/blob/main/Data%20Scraping/screenshot/program-4.png" width="50%">

#### Program 5 Mengambil Data Restoran dari Page 31-40

<img src="https://github.com/roscellyn/Seleksi-2021-Tugas-1/blob/main/Data%20Scraping/screenshot/program-5.png" width="50%">

#### Data Setelah Seluruh Program Selesai Dijalankan

<img src="https://github.com/roscellyn/Seleksi-2021-Tugas-1/blob/main/Data%20Scraping/screenshot/data-after.png" width="50%">

### Data Storing

#### Import Data ke MongoDB

<img src="https://github.com/roscellyn/Seleksi-2021-Tugas-1/blob/main/Data%20Storing/screenshot/import-data.png">

#### Access Data dari MongoDB

<img src="https://github.com/roscellyn/Seleksi-2021-Tugas-1/blob/main/Data%20Storing/screenshot/imported-data.png" width="50%">

#### Export Data dari MongoDB

<img src="https://github.com/roscellyn/Seleksi-2021-Tugas-1/blob/main/Data%20Storing/screenshot/export-data.png">

#### Import Data ke MongoDB Atlas

<img src="https://github.com/roscellyn/Seleksi-2021-Tugas-1/blob/main/Data%20Storing/screenshot/import-data-online.png">

#### Access Data via API

<img src="https://github.com/roscellyn/Seleksi-2021-Tugas-1/blob/main/Data%20Storing/screenshot/access-data-via-api.png" width="50%">

## References

### Data Scraping

Berikut daftar library yang digunakan beserta referensi lainnya:

1. BeautifulSoup

- https://pypi.org/project/beautifulsoup4/

2. requests

- https://pypi.org/project/requests/

3. json

- https://www.geeksforgeeks.org/append-to-json-file-using-python/

4. time

- https://docs.python.org/3/library/time.html

5. Referensi lainnya <br />

Website untuk data scraping:

- https://pergikuliner.com/restaurants?utf8=%E2%9C%93&search_place=&default_search=Jakarta&search_name_cuisine=&commit=

Panduan data scraping:

- http://bit.ly/DataScrapingGuidance

Link tutorial Youtube:

- https://www.youtube.com/watch?v=XVv6mJpFOb0&ab_channel=freeCodeCamp.org

### Data Storing

- https://docs.mongodb.com/v4.2/reference/program/mongoexport/
- https://www.youtube.com/watch?v=Phe9B2HRVmc&t=101s&ab_channel=PraveenKumar
- https://github.com/beaucarnes/mern-exercise-tracker-mongodb/tree/master/backend

## Author

Jacelyn Felisha <br />
18219097 <br />
Sistem dan Teknologi Informasi ITB 2019
