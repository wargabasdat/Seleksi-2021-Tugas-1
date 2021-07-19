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


## Spesifikasi

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
  Selamat Mengerjakann
  <br>
  <br>
</h3>
