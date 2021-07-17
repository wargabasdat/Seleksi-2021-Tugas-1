# WebScraping Pemain Liga 1 Indonesia 2021 / 2022 
Webscraping dari situs [(https://www.transfermarkt.com/liga-1-indonesia/startseite/wettbewerb/IN1L)](https://www.transfermarkt.com/liga-1-indonesia/startseite/wettbewerb/IN1L).
Tujuan dari webscraping ini adalah untuk mendapatkan data Tim-tim sepakbola Liga 1 Indonesia musim 2021/2022 beserta data pemainnya. 
 
*disclaimer : this program is for educational purposes*
## Spesifikasi
- Pada laman [(https://www.transfermarkt.com/liga-1-indonesia/startseite/wettbewerb/IN1L)](https://www.transfermarkt.com/liga-1-indonesia/startseite/wettbewerb/IN1L) terdapat daftar Tim, juga link yang menuju detail dari Tim tersebut. Sebagai contoh untuk detail dari pemain Persib Bandung terlihat pada link berikutt [https://www.transfermarkt.com/persib-bandung/kader/verein/14105/saison_id/2020/plus/1](https://www.transfermarkt.com/persib-bandung/kader/verein/14105/saison_id/2020/plus/1)
- Setelah ditelaah tag html pada laman, kemudian didapat pengetahuan untuk membentuk struktur data json sebagai berikut

### Clubs
| Atribut 	| Tipe         	|
|---------	|--------------	|
| id      	| Integer      	|
| name    	| VARCHAR      	|
| manager 	| VARCHAR      	|
| league  	| VARCHAR      	|
| stadium 	| VARCHAR      	|

### Players
| Atribut       	| Tipe    	|
|---------------	|---------	|
| id            	| INT     	|
| name          	| VARCHAR 	|
| number        	| VARCHAR 	|
| position      	| VARCHAR 	|
| birth-of-date 	| DATE    	|
| nationality   	| VARCHAR 	|
| height        	| VARCHAR 	|
| foot          	| VARCHAR 	|
| market-value  	| VARCHAR 	|
| club          	| VARCHAR 	|


## Cara Menggunakan
- Pastikan python3 dan pip terinstall
- Install semua dependencies dengan command `pip install -r requirements.txt`
- File `scrapping.py` digunakan untuk melakukan scrapping data dari situs transfermrkt. Kemudian menyimpannya pada file `scrap.json`
- Pada file `setupDb.py`, jalankan file ini dengan terlebih dahulu mengkonfigurasi file `.env`. File ini digunakan untuk inisialisasi database dan membuat table `clubs` dan `players`
- Pada file `dbConn.py`, menjalankan input data `scrap.json` ke database. Jika terdapat `file/directory not found`, dapat menyesuaikan dengan path yang benar pada bagian `# Load JSON file. 


## Struktur JSON
- `data` sebagai array dictionary berisi `clubs` dan `players`
- Key `clubs` merupakan array yang isinya array dictionary. Berisi data club-club sepakbola Liga 1 Indonesia. Dengan key attributes *id, name, manager, league, stadium*
- Key `players` merupakan array yang isinya array dictionary. Berisi data pemain dari setiap klub Liga 1 Indonesia. Dengan key attributes *id, name, number, position, date-of-birth, nationality, height, foot, market-value, club*

## Screenshot

### Web Scraping
![Tangkapan layar 1](/Data%20Scraping/screenshot/1.png)  

### DBMS MariaDb
![Tangkapan layar 1](/Data%20Storing/screenshot/1.png)  
![Tangkapan layar 2](/Data%20Storing/screenshot/2.png)  

## Reference
Library lain
- beautifulsoup4
- lxml
- python-decouple
- mysql-connector-python

## Hosting Online
- [https://www.freemysqlhosting.net/](https://www.freemysqlhosting.net/)
- [https://www.000webhost.com/](https://www.000webhost.com/)

## Author
[Muhammad Jafar - 13519197](https://github.com/mhmmdjafarg) 

📌 Bandung, Indonesia