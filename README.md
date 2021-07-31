# Description of the data and DBMS

Data ini adalah data list pekerjaan _Software Engineer_ dari Glints, sebuah platform untuk mencari pekerjaan. Pada tugas ini saya menggunakan list pekerjaan yang terdapat di Jakarta dan terbatas hanya pekerjaan _Software Engineer_ saja.

Untuk DBMS, yang dipakai adalah MongoDB karena merupakan database yang sudah lazim dipakai saat ini. Juga saya pernah menggunakan MongoDB untuk mengerjakan tugas Stima.

# Specification of the program

## Problem Statement

Di masa pandemi ini, banyak perusahaan yang mulai membuka lowongan pekerjaan di bidang teknologi, khususnya _software engineer_ pada platform pencari kerja seperti Glints. Akan tetapi, pekerjaan yang tertera pada Glints tidak semuanya dapat diambil dan jumlah pekerjaan yang tertera pada Glints tidak mungkin akan dicek satu per satu secara manual. Oleh karena itu dibuatlah program web scraping yang akan menyimpan list pekerjaan dan info pentingnya seperti posisi, nama perusahaan, gaji, dan lainnya.

## How The Program Works

1. Pertama program ini memuat halaman HTML yang ingin dituju menggunakan selenium dengan bantuan webdriver chrome, karena halaman Glints adalah website dinamis yang menggunakan _infinite scrolling load_ sehingga untuk memuat lebih banyak data pekerjaan harus menggunakan selenium.
2. Setelah menggunakan selenium, HTML tersebut diparse dan dicari berdasarkan tag dari HTML menggunakan library BeautifulSoup untuk mencari tag dan class yang dibutuhkan.
3. Setelah mendapatkan data teks yang dibutuhkan, hasil dari scraping tersebut kemudian disimpan dalam format json per kartunya.

![image](https://github.com/alvinwilta/Seleksi-2021-Tugas-1/tree/main/Data%20Scraping/screenshot/glints.PNG)
![image](https://github.com/alvinwilta/Seleksi-2021-Tugas-1/tree/main/Data%20Scraping/screenshot/python.PNG)

start the server

```
mongod --dbpath "dir/to/db" --port 27017
```

start data scraping

```
python Data\ Scraping/src/main.py
```

start exporting it to db and dumping it to local folder

```
python Data\ Scraping/src/export.py
```

# JSON Structure

```
"title": posisi pekerjaan
"company": perusahaan yang menawarkan posisi
"location": lokasi pekerjaan
"estimate_salary": Estimasi gaji
"exp_min": pengalaman kerja minimal (tahun)
"exp_opt": lama pengalaman kerja optimal (tahun)
"last_updated": kapan terakhir kali pekerjaan diupdate
"applicant": jumlah pendaftar
```

# Reference

External Libraries Used:

- BeautifulSoup v0.0.1
- lxml v4.5.2
- Selenium v3.141.0

# Author

Alvin Wilta 13519163 - [Github](https://github.com/alvinwilta)

# Disclaimer

Saya meminta maaf yang sebesar-besarnya atas kelalaian dalam mengatur waktu dan mengumpulkan tugas mendekati deadline. Kesalahan ini tidak akan terulang kembali, terima kasih.
