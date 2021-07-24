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

# Seleksi Warga Basdat 2021
> Tugas 1 : Data Scraping & Data Storing


## Table of contents
* [Description of the data and DBMS](#Description-of-the-data-and-DBMS)
* [Specification of the program](#Specification-of-the-program)
* [Clone Repository](#clone-repository)
* [How To Use](#how-to-use)
* [JSON Structure](#json-structure)
* [Screenshot program](#Screenshot-program)
* [Reference](#Reference)
* [Common Error](#common-error)
* [Author](#Author)


## Description of the data and DBMS
Pada tugas seleksi kali ini, author menggunakan data film dari imdb. Spesifiknya data tentang film action-hero. Saat akan meluncurkan sebuah film ataupun film telah tayang. Tentu film akan memiliki data seperti judul, deskripsi, rating, durasi, genre, dan lain lain. 
Seperti yang kita ketahui, data imdb telah memiliki api nya sendiri, sehingga tidak masalah jika melakukan scraping pada website ini. Kendati demikian, sebagai seorang yang ingin melakukan scraping, harus mematuhi terlebih dahulu etika dalam melakukan scraping. 
DBMS yang digunakan pada tugas kali ini adalah mongoDB. Dipilihnya mongoDB karena author menganggap database ini cukup flexible, mengingat mongoDB merupakan database NOSQL. MongoDB juga menggunakan file JSON sehingga akan lebih mudah untuk author mengintegrasikannya. Pada era yang semakin canggih ini, database NOSQL seperti MongoDB semakin banyak penggunanya. Oleh karenanya pada tugas kali ini, author memilih mongoDB sebagai database.


## Specification of the program

### Data Scraping

1. Lakukan _data scraping_ dari sebuah laman web untuk memperoleh data atau informasi tertentu __TANPA MENGGUNAKAN API__. Hasil _data scraping_ ini nantinya akan disimpan dalam DBMS dan digunakan sebagai bahan tugas analisis dan visualisasi data.

2. Daftarkan judul topik yang akan dijadikan bahan _data scraping_ dan DBMS yang akan digunakan pada spreadsheet berikut: [Topik Data Scraping](https://docs.google.com/spreadsheets/d/12sgizyreDkFXz4N3FaGouyGKRZN3qHyWEeSIbEXtpR4/edit?usp=sharing). Usahakan agar tidak ada peserta dengan topik yang sama. Akses edit ke spreadsheet akan ditutup tanggal __12 Juli 2021 pukul 23.59 WIB__

3. Pada folder `Data Scraping`, calon warga basdat harus mengumpulkan _file script_, json hasil _data scraping_. Folder `Data Scraping` terdiri dari _folder_ `src`, `data` dan `screenshots`. 
    - _Folder_ `src` berisi _file script_/kode yang __*WELL DOCUMENTED* dan *CLEAN CODE*__ 
    - _Folder_ `data` berisi _file_ json hasil _scraper_
    - _Folder_ `screenshot` berisi tangkapan layar program.

4. Sebagai referensi untuk mengenal _data scraping_, asisten menyediakan dokumen "_Short Guidance To Data Scraping_" yang dapat diakses pada link berikut: [Data Scraping Guidance](http://bit.ly/DataScrapingGuidance). Mohon memperhatikan etika dalam melakukan _scraping_.

5. JSON harus dinormalisasi dan harus di-_preprocessing_
```
Preprocessing contohnya :
- Cleaning
- Parsing
- Transformation
- dan lainnya
```

### Data Storing

1. Lakukan _storing_ data yang didapatkan dari hasil _scraping_ ke DBMS 

2. Tools yang digunakan __dibebaskan__

3. Calon warga basdat harus mengumpulkan bukti penyimpanan data pada DBMS. _Folder_ `Data Storing` terdiri dari folder `data`, `screenshots` dan `export`
    - _Folder_ `screenshot` berisi tangkapan layar bukti dari penyimpanan data ke DBMS
    - _Folder_ `export` berisi _file_ hasil _export_ dari DBMS (seperti `.sql`, `.json`, (1 saja yang didukung oleh DBMS))



4. Task-task berikut bersifat tidak wajib (__BONUS__), boleh dikerjakan sebagian atau seluruhnya
    - Simpan ke database online
    - Buatlah API sederhana untuk mengakses database online tersebut

### Pengumpulan

1. Dalam mengerjakan tugas, calon warga basdat terlebih dahulu melakukan _fork_ project github pada link berikut: [Seleksi-2021-Tugas-1](https://github.com/wargabasdat/Seleksi-2021-Tugas-1). Sebelum batas waktu pengumpulan berakhir, calon warga basdat harus sudah melakukan _pull request_ dengan nama ```TUGAS_SELEKSI_1_[NIM]```

2. Tambahkan juga `.gitignore` pada _file_ atau _folder_ yang tidak perlu di-_upload_, __NB: BINARY TIDAK DIUPLOAD__

3. Berikan satu buah file `README` yang __WELL DOCUMENTED__ dengan cara __override__ _file_ `README.md` ini. `README` harus memuat minimal konten:


```
- Description of the data and DBMS (Why you choose it)
- Specification of the program
- How to use
- JSON Structure
- Screenshot program (di-upload pada folder screenshots, di-upload file image nya, dan ditampilkan di dalam README)
- Reference (Library used, etc)
- Author
```


4. Deadline pengumpulan tugas 1 adalah <span style="color:red">__24 Juli 2021 Pukul 23.59 WIB__</span>

<h3 align="center">
  <br>
  Selamat Mengerjakan
  <br>
  <br>
</h3>

<br>
<br>


## Clone Repository
1. Buka terminal (gitbash, cmd, terminal vscode), lalu arahkan ke folder yang ingin digunakan menyimpan repository
2. Lakukan clone git dengan cara lakukan (git clone https://github.com/dwibagus154/Seleksi-2021-Tugas-1.git) pada terminal
3. Setelah proses cloning selesai Anda dapat keluar dari terminal
4. Pergi ke folder hasil clone repository lalu buka di text editor kesayangan anda
5. Repository sudah dapat digunakan


## How to Use
Menggunakan Scraping
1. Pergi ke folder repository yang telah di clone, dan buka folder di text editor kesayangan anda (pastikan folder root dalam text editor adalah SELEKSI-2021-TUGAS-1)
2. Buka file Data Scraping/src/scrap.py pada text editor
3. pastikan internet telah berjalan, karena menggunakan DATABASE ONLINE dan pastikan juga telah menginstall python (bisa install di https://www.python.org/)
4. Buka terminal kesayangan anda (diharapkan yang menggunakan vscode langsung saja di terminal vscode)
5. install requirement yang diperlukan seperti pymongo, beautifulsoap, json, request (jika kurang bisa lihat di line import pada setiap file atau di pesan error pada terminal, lalu ketikkan pip install <nama-requirement>)
5. jalankan program scrap.py atau anda bisa ketikkan python "Data Scraping/src/scrap.py" pada terminal , sehingga file json yang ada di Data Scraping/data/data.json akan diperbaharui
6. Pastikan saat menjalankan program, folder root dalam text editor kita adalaha SELEKSI-2021-TUGAS-1
7. Pada scraping kali ini, data yang author ambil hanya 20 page(1000 data), anda bisa menggantinya jumalhpage yang mau di scraping pada file scrap.py (line 93) menjadi angka lain (1 sampai 50, jangan sampai lebih dari 50)

Menggunakan API 
1. Buka folder api yang ada di dalam folder Data Scraping/src di text editor baru(pastikan folder api menjadi folder root di text editor)
2. install requirement yang diperlukan seperti flask, pymongo, bson (jika kurang bisa lihat di line import pada setiap file atau di pesan error pada terminal, lalu ketikkan pip install <nama-requirement>)
3. Buka Postman atau aplikasi sejenisnya untuk melakukan CRUD (bisa install disini https://www.postman.com/)
4. lalu jalankan aplikasi dengan ketikkan flask run di terminal 
5. masukkan endpoint pada aplikasi postman atau sejenisnya (tidak bisa menggunakan browser untuk method selain get)
* http://127.0.0.1:5000/api/v1/imdb dengan method get untuk ambil semua data 
* http://127.0.0.1:5000/api/v1/imdb dengan method post, lalu isi data untuk menambah data 
* http://127.0.0.1:5000/api/v1/imdb/<<filmid>> dengan method get untuk ambil data dengan id tertentu 
* http://127.0.0.1:5000/api/v1/imdb/nama/<<title>> dengan method get untuk ambil data dengan title tertentu
* http://127.0.0.1:5000/api/v1/imdb/<<filmid>> dengan method put untuk update data dengan id tertentu
* http://127.0.0.1:5000/api/v1/imdb/<<filmid>> dengan method delete untuk delete data dengan id tertentu


## JSON Structure
1. title, bertipe string
2. description, bertipe string
3. rating, bertipe integer
4. genre, bertipe string
5. time, bertipe string
6. certificate, bertipe string

## Screenshot program


## Reference
* https://www.python.org/
* https://www.postman.com/
* https://www.mongodb.com/
* https://pymongo.readthedocs.io/
* https://www.crummy.com/software/BeautifulSoup/bs4/doc/

## Common Error
* Pada saat menjalankan, folder root bukan folder SELEKSI-2021-TUGAS-1 sehingga terdapat kendala dalam mengakses path file json
* Pada saat menjalankan API, folder root bukan folder api yang terdapat dalam folder Data Scraping/src, sehingga aplikasi tidak bisa dijalankan
* Belum install requirements, lihat baik baik pada error terminal requirement apa yang pelum, lalu ketikkan di terminal pip install 
<nama-requirement>

## Author
* 13519057 Kadek Dwi Bagus Ananta Udayana