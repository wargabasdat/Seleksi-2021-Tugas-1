<h1 align="center">
  <br>
  Data Mobil Bekas di Indonesia
  <br>

</h1>

<h2 align="center">
  <br>
  Data Scraping & Data Storing dari Mobil123.com
  <br>
  <br>
</h2>

- Topik yang saya pilih untuk dilakukan data scraping adalah pengambilan data mobil bekas, dimana data mobil bekas ini saya ambil dari sebuah *website* bernama [Mobil123](https://www.mobil123.com). Dengan adanya data mengenai mobil bekas ini, diharapkan dapat membantu pihak-pihak yang saat ini sedang ingin membeli mobil bekas atau bagi pihak yang ingin menjual mobil miliknya.

- DBMS yang saya gunakan untuk menyimpan dan meng-*export* data hasil scraping adalah [MongoDB](https://www.mongodb.com). MongoDB adalah sebuah *document-oriented* DBMS yang menggunakan dokumen-dokumen seperti .JSON, dengan skema yang bersifat opsional. MongoDB termasuk salah satu dari kelompok NoSQL DBMS. DBMS dapat menangani import dan export untuk file .JSON dengan mudah, serta schema yang disediakan sangat bebas tergantung kebutuhan pengguna. Selain itu, dikarenakan kurang adanya kebutuhan relasi antar data yang saya miliki, menurut saya akan kurang tepat jika DBMS yang digunakan adalah tipe RDBMS.

- Pada folder Data Scraping, terdapat sebuah program yang tersimpan dalam /src, yaitu _*main.py*_
- Terdapat juga sebuah file API pada folder Data Storing, yang tersimpan dalam /bonus, dengan nama file _*api.js*_

#### File Script main.py

- Program ini pada dasarnya bertugas untuk melakukan scraping data dari website [Mobil123](https://www.mobil123.com). Program ini menggunakan bahasa Python.

- Beberapa library yang digunakan untuk menjalankan program ini adalah sebagai berikut:
```
  - requests
  - os
  - json
  - pandas
  - bs4(beautifulsoup4)
```
- Pertama-tama, beberapa library tersebut harus diinstal terlebih dahulu, karena merupakan external library yang tidak ikut terinstall dengan python. Library tersebut adalah requests, pandas, dan bs4. Instalasi dapat dilakukan dengan perintah berikut pada cmd:
```
pip install beautifulsoup4 pandas requests
```
- Program ini akan melakukan scraping data dan menyimpan hasilnya pada sebuah local file dengan ekstensi .json.

- Saat program berjalan, pertama-tama user akan diminta untuk memberikan nama untuk file .json yang akan menyimpan hasil scraping data.

- Kemudian, program akan mengambil data yang sesuai dengan kriteria pada fungsi get_mobil_data(). Setiap data mobil yang diambil akan disimpan dalam sebuah dictionary, dan kemudian seluruh dictionary yang tercipta ditambahkan ke dalam sebuah array.

- Terakhir, jika file dengan nama yang dimasukkan oleh pengguna belum ada, maka akan dibuat file .json dengan nama tersebut, dan menambahkan data array dengan format json. Pada lain kasus, jika sudah ada file dengan nama yang dimasukkan pengguna, maka isi dari file tersebut akan diupdate dengan data array yang baru.
![program](.\Data%20Scraping\screenshot\program.png?raw=true)
- Scraping dapat dijalankan dengan menggunakan perintah
```
python -u "file/path/to/main.py"

dimana file/path/to adalah path dari file main.py tersimpan
```
![ssprogram](.\Data%20Scraping\screenshot\ssprogram.png?raw=true)
- Program ini juga terdiri atas beberapa fungsi pendukung seperti get_mobil_data(), format_distance(), dan beberapa fungsi lain.

- JSON Structure dari program main.py adalah sebagai berikut:
```
{
  TipeMobil      : String,
  Tahun          : String,
  Harga          : String,
  Jarak          : String,
  Transmisi      : String,
  Lokasi         : String,
  Penjual        : String
}
```

####  Local Data Storing

- Secara singkat, proses yang dilakukan untuk melakukan importing data pada MongoDB adalah mengambil data yang dihasilkan oleh script _*main.py*_ menggunakan sebuah library _mongoimport_.
  - _Mongoimport_ dapat diinstal melalui MongoDB Database Tools, yang dapat diunduh pada link berikut [_*ini*_](https://www.mongodb.com/try/download/database-tools)
  - Buka cmd/shell baru, kemudian ketikkan perintah
  ```
  mongod
  ```
  ![mongod](.\Data%20Storing\screenshot\mongod.png?raw=true)
  - Setelah _MongoImport_ terinstal, buka cmd dan pergi pada folder dimana _Tools_ tersebut berada, kemudian cari dan pergi ke folder bin di _Tools_ tersebut.
  Untuk melakukan import data ke dalam NoSQL DBMS MongoDB, kemudian melakukan export data yang sudah diimport tersebut ke dalam sebuah file .json, kita dapat menggunakan dua perintah berikut
  ![import_export_data](.\Data%20Storing\screenshot\import_export.png?raw=true)
  - Kita dapat mengecek apakah data kita sudah terimport atau belum di MongoDB dengan serangkaian perintah berikut.
  ```
  > mongo
  > show dbs
  > use [selectedDb]
  > show collections
  > db.[collectionUsed].find()
  ```
  ![data_on_db](.\Data%20Storing\screenshot\data_on_db.png?raw=true)

  - Seperti terlihat pada beberapa langkah sebelumnya, data dieskpor ke dalam sebuah file bernama _*exportedData.json*_. (ditunjukkan di window sebelah kiri)
  ![exportedData](.\Data%20Storing\screenshot\exportedData.png?raw=true)

- Struktur JSON pada file hasil export MongoDB juga tidak jauh berbeda, yaitu dengan tambahan _id saja.
```
{
  _id            : {
    $oid            : String
  },
  TipeMobil      : String,
  Tahun          : String,
  Harga          : String,
  Jarak          : String,
  Transmisi      : String,
  Lokasi         : String,
  Penjual        : String
}
```

#### api.js

- File ini berisi penyelesaian dari bonus, yaitu API sederhana untuk mengakses data yang disimpan pada database online.

- Sebelum membahas terkait API terlebih dahulu, mari membahas tentang cara mengimport file .json kita ke database online yang digunakan, yaitu MongoDB Atlas
  - Pertama, mari kita buat sebuah free cluster di MongoDB Atlas
  - Kemudian, kita lakukan konfigurasi terhadap network access dan database access.
    - Pada network access, kita menambahkan sebuah IP Address configuration dengan konfigurasi sebagai berikut.
    ![userAccess](.\Data%20Storing\bonus\screenshot\online_db\db_access.png?raw=true)
    - Pada database access, kita menambahkan sebuah user yang memiliki *role* sebagai _Atlas Admin_ dan memberikan password untuk role tersebut.
    ![networkAccess](.\Data%20Storing\bonus\screenshot\online_db\network_access.png?raw=true)
  - Kemudian, setelah cluster siap untuk digunakan, kita akan mencoba untuk melakukan test terhadap koneksi database pada shell
    - Pilih Connect -> Connect to a MongoDB Shell -> Copy connection String pada shell/cmd -> Masukkan password user pada cmd
    ![connectShell](.\Data%20Storing\bonus\screenshot\online_db\connect_shell.png?raw=true)
    - Berikut adalah hasilnya
    ![dbConnect](.\Data%20Storing\bonus\screenshot\online_db\db_connect.png?raw=true)
    - Terakhir, kita siap untuk mengimport data yang berada pada file exportedData.json menuju ke MongoDB Atlas
      - Pertama, kita mencari shard yang berada pada cluster kita. List ini dapat kita akses pada <NamaCluster> -> Overview. Kemudian, kita memilih shard yang memiliki role primary. Role tersebut akan disalin namanya dan digunakan sebagai host
      ![host](.\Data%20Storing\bonus\screenshot\online_db\host.png?raw=true)
      ![primaryHost](.\Data%20Storing\bonus\screenshot\online_db\primary_host.png?raw=true)
      - Selanjutnya, kita menjalankan perintah penyimpanan yang mirip seperti menyimpan pada local database.
      ![data_imported](.\Data%20Storing\bonus\screenshot\online_db\import_data.png?raw=true)
      - Kita dapat melihat data yang baru saja diimport melalui shell
      ![new_data_imported](.\Data%20Storing\bonus\screenshot\online_db\show_data.png?raw=true)

- API ini dibangun dengan menggunakan NodeJS dengan ExpressJS dan beberapa library yang diinstal melalui npm. Library tersebut diantaranya adalah :
```
  - Express
  - Mongoose
  - Lodash
  - Nodemon (optional)
```

- Untuk menginstall library-library tersebut, kita cukup menggunakan perintah ini pada cmd:
```
npm i --save express mongoose lodash
```
- Sebelum menuliskan apapun pada program, ada baiknya kita melakukan perintah
```
npm init -y
```
pada cmd terlebih dahulu.

- Pertama-tama, kita inisiasi dengan Express() untuk membuat aplikasi menggunakan ExpressJS

- Selanjutnya adalah untuk menghubungkan aplikasi dengan cluster MongoDB Atlas yang telah kita buat, dan dilanjutkan dengan membuat sebuah skema untuk collection yang digunakan. Selanjutnya, sebuah model/collection dibuat berdasarkan schema yang sudah didefinisikan.

- Kemudian, akan dilanjutkan dengan menentukan pada port mana API akan berjalan.
```
app.listen(3000, () => console.log("Server started on port 3000"));
```
Pada cuplikan kode tersebut, saya telah menentukan API untuk berjalan pada port 3000. Untuk mengakses alamat API, kita dapat menggunakan alamat *localhost:3000*, tetapi tidak ada fungsionalitas yang bisa didapatkan dari alamat tersebut.

- Pada API yang telah saya buat, saya telah menciptakan beberapa fungsionalitas untuk mendapatkan data sesuai kriteria-kriteria tertentu. Di antaranya adalah sebagai berikut:
```
  - localhost:3000/cars
    => Mengakses seluruh data mobil bekas
  - localhost:3000/cars/jarak/min_length=:minMileage/max_length=:maxMileage
    => Mengakses data mobil bekas berdasarkan rentang jarak tempuh yang dimasukkan pengguna.
  - localhost:3000/cars/year/:carYear
    => Mendapatkan data dari mobil yang merupakan produk keluaran dari suatu tahun tertentu
  - localhost:3000/cars/penjual/:penjual
    => Menampilkan data dari mobil bekas yang memiliki tipe penjual tertentu
  - localhost:3000/cars/lokasi/:lokasi
    => Menampilkan data dari mobil bekas yang dijual pada suatu provinsi tertentu saja
  - localhost:3000/cars/transmisi/:transmission
    => Menampilkan data mobil bekas yang memiliki transmisi tertentu saja
  - localhost:3000/cars/harga/max_harga=:hargaJual
    => Menampilkan data mobil bekas yang memiliki harga tidak lebih tinggi dari harga masukan pengguna
  - localhost:3000/cars/harga/min_harga=:hargaJual
    => Menampilkan data mobil bekas yang memiliki harga tidak lebih rendah dari harga masukan pengguna
  - localhost:3000/cars/harga/min_harga=:batasBawah/max_harga=:batasAtas
    => Menampilkan data mobil bekas yang memiliki harga pada rentang min_harga-max_harga
  - localhost:3000/cars/brand/:brandName
    => Menampilkan data mobil bekas yang diproduksi oleh brand tertentu saja (e.g. Mercedes-Benz, Toyota, dll)
```
- Untuk menjalankan API ini,
  - pertama-tama, buka cmd dan pergi ke folder dimana terdapat file _api.js_ ini.
  - Kemudian, ketikkan perintah
  ```
  npm i
  ```
  dan npm akan mengunduh seluruh library yang dibutuhkan oleh API ke dalam environment Anda
  - Anda siap untuk menjalankan API, ketikkan perintah berikut.
  ```
  nodemon api.js    // jika Anda telah memiliki library nodemon terinstal, atau

  node api.js
  ```
- Untuk detil fungsionalitas dan kode, silakan akses file api.js pada folder Data Storing -> bonus
- Di bawah ini adalah dokumentasi API saat dijalankan

![runningAPI](.\Data%20Storing\bonus\screenshot\API\run_api.png?raw=true)

![cars](.\Data%20Storing\bonus\screenshot\API\all_cars.png?raw=true)

![car_by_distance](.\Data%20Storing\bonus\screenshot\API\distance_cars.png?raw=true)

![car_by_year](.\Data%20Storing\bonus\screenshot\API\car_year.png?raw=true)

![car_by_location](.\Data%20Storing\bonus\screenshot\API\car_location.png?raw=true)

![car_by_seller](.\Data%20Storing\bonus\screenshot\API\car_seller.png?raw=true)

![car_by_brand](.\Data%20Storing\bonus\screenshot\API\brand_car.png?raw=true)

![car_by_transmission](.\Data%20Storing\bonus\screenshot\API\car_transmission.png?raw=true)

![car_by_maxPrice](.\Data%20Storing\bonus\screenshot\API\maxPrice_car.png?raw=true)

![car_by_minPrice](.\Data%20Storing\bonus\screenshot\API\minPrice_car.png?raw=true)

![car_by_price](.\Data%20Storing\bonus\screenshot\API\price_car.png?raw=true)

#### Referensi
- [_*PyPI*_](https://pypi.org/) - Dokumentasi dari seluruh library yang digunakan pada Python
- [_*npm*_](https://www.npmjs.com/) - Dokumentasi dan detail dari seluruh library yang digunakan oleh API yang saya buat
- [_*Web Scraping Menggunakan BeautifulSoup*_](https://www.youtube.com/watch?v=XVv6mJpFOb0) - Sebuah tutorial mengenai penggunaan BeautifulSoup untuk keperluan web scraping
- [_*Stack Overflow*_](https://stackoverflow.com/) - Berbagai forumnya yang memecahkan masalah yang dihadapi pada proses pengerjaan
- [_*MongoDB Docs*_](https://docs.mongodb.com/) - Dokumentasi penggunaan MongoDB


#### Baskoro Adi Wicaksono / 18219113
#### Institut Teknologi Bandung