<h1 align="center">
  <br>
  Billboard Web Scrapper
  <br>
  <br>
</h1>

## Deskripsi
Program untuk web scraping dari https://www.billboard.com/charts/ dengan mengambil 3 chart yang tersedia secara _free_:
```
1. The Hot 100    : https://www.billboard.com/charts/hot-100
2. Artist 100     : https://www.billboard.com/charts/artist-100/
3. Billboard 200  : https://www.billboard.com/charts/billboard-200
```
Web Billboard dipilih karena merupakan salah satu penyedia _music chart_ yang paling dikenal di dunia sehingga dari data yang berhasil didapatkan dapat menghasilkan informasi yang lebih _advance_.

## Spesifikasi Program
Program dibuat dengan bahasa Python dengan menggunakan library BeautifulSoup. 

## How to use
Run program pada terminal:
```
python "Data Scraping\src\main.py"
```

## JSON Structure
Struktur JSON berbeda-beda untuk setiap chart. Secara umum struktur terdiri dari:
* `fetchTime` &ndash; waktu pengambilan data chart
* `chartWeek` &ndash; tanggal chart di-_release_
* `chart` &ndash; list berisi elemen dari chart


## Screenshot Program


## Reference
Library yang digunaan:
* `BeautifulSoup`
* `requests`
* `time`
* `datetime`
* `os`
* `json`

## Author
Bonaventura Bagas Sukarno - 18219017
