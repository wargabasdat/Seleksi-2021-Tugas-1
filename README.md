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

**Start the server**

```
mongod --dbpath "dir/to/db" --port 27017
```

**Start data scraping**

```
python Data\ Scraping/src/main.py
```

**Start exporting it to db and dumping it to local folder**

```
python Data\ Scraping/src/export.py
```

## Images

<details>
    <summary><b>Glints Job Portal</b></summary>
    <img src="./Data Scraping/screenshot/glints.PNG" alt="Glints Job Portal">
</details>
<details>
    <summary><b>Python Scraping Program Ouput Log</b></summary>
    <img src="./Data Scraping/screenshot/terminal.PNG" alt="Program terminal output">
</details>
<br>
<details>
    <summary><b>Python Export Program Ouput Log (if error)</b></summary>
    <img src="./Data Storing/screenshot/terminal_error.PNG" alt="Program terminal error output">
</details>
<details>
    <summary><b>Python Export Program Ouput Log (if successful)</b></summary>
    <img src="./Data Storing/screenshot/terminal_success.PNG" alt="Program terminal success output">
</details>
<details>
    <summary><b>Collection Structure in MongoDB</b></summary>
    <img src="./Data Storing/screenshot/database.PNG" alt="MongoDB database">
</details>
<br>

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

Presentasi:

- Visualisasi Data
- Hasil analisis data (informasi apa yang bisa didapat)
- Insight yang bisa didapatkan dari informasi tersebut
- query yang digunakan untuk mendapat insight (pake tabel digabung2)
