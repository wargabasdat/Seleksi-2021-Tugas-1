<h1 align="center">
  <br>
  Data Scraping & Data Storing
  <br>
  <br>
</h1>

<img src="./Data Scraping/screenshot/1.png"/>

## Deskripsi

### A. Data
Dalam Repo ini, saya membuat sebuah program _data scraping_ pada web [Yankes Siranap](https://yankes.kemkes.go.id/app/siranap/). Data yang di-_collect_ dari website ini adalah data profil rumah sakit di Indonesia berupa Nama, Alamat, Nomor Telepon, Jumlah Bed Kosong, Link profil yang lebih lengkap. 

Alasan pemilihan data ini adalah selama pandemi ini banyak sekali orang yang membutuhkan informasi mengenai data rumah sakit. Jika nanti ini dikembangkan nantinya bisa membuat API yang databasenya diupdate berkala untuk membuat lebih banyak orang dapat mengembangkan platform informasi ini

### B. Database

Database yang digunakan dalam tugas ini adalah MongoDB. MongoDB merupakan database yang termasuk kedalam NoSQL. Dengan tipe document database, selain itu MongoDB melalui [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) melakukan gerakan serverless. Yaitu penggunaan database sebagai SAAS (Software as a service) sehingga mempermudah connect kedalam aplikasi dengan mudah.

#### __Kenapa menggunakan Database ini?__

Saya menggunakan MongoDB, karena saya ingin melakukan __eksplorasi__ dengan MongoDB dalam tugas ini. Selain itu, saya tertarik dengan MongoDB yang menyimpan data dengan bentuk JSON sehingga dalam collection atau table di Database Realtional bisa leluasa karena recordnya mempunyai kebebasan sehingga bisa menyimpan dengan fields yang berbeda. Bayangkan saja dalam satu collection/table isi recordnya bisa seperti id 1 isi fieldnya "name","email",dan "password", sedangkan record kedua berisi "email",dan "password". Importnya juga mudah karena berupa JSON files dan bisa export ke JSON maupun CSV.



## Spesifikasi

Program ini dijalankan menggunakan bahasa pemrograman Golang. Kenapa Golang? Karena saya ingin belajar eksplorasi bahasa pemrograman GO. Dengan menggunakan libraries, Sebagai berikut `Colly` untuk melakukan webscrapping. Dengan colly ini lebih mudah karena menggunakan queryselector CSS untuk melakukan Scrapping. Dan `Gin` untuk mempermudah pembuatan `Rest API` sehingga semudah menggunaka `Express` pada `Node JS`. Untuk menjalankan harap telah menginstall Golang atau Docker

### _Inovasi_

Untuk mempermudah penggunaan aplikasi untuk device yang belum menginstall GO, Saya mengunakan Docker untuk mempermudah penggunaan aplikasi


## How to Use

### A. Data Scraping
#### __Menggunakan Docker__ 

1. Run command pada terminal
```cmd
cd "Data Scraping/src
```
2. Jalankan Docker pada OS
3. Run command pada terminal
```cmd
docker-compose up
```
4. Tunggu sampai program exit
<img src="./Data Scraping/screenshot/2.png"/>

5. Akan digenerate 2 file yaitu hospital.json dan province.json
<img src="./Data Scraping/screenshot/3.png"/>

6. Terakhir exit image dengan run command
```cmd
docker-compose down
```
#### __Tanpa Docker__ 
1. Run command pada terminal
```cmd
cd "Data Scraping/src
```
2. Run command
```cmd
go mod download
```
3.Run command
```cmd
go run main.go
```
4. Tunggu sampai program exit
<img src="./Data Scraping/screenshot/4.png"/>

5. Akan digenerate 2 file yaitu hospital.json dan province.json
<img src="./Data Scraping/screenshot/3.png"/>

## JSON Structure

Tiap _record_ dalam JSON File hasil proses _data scraping_ ini memiliki atribut-atribut sebagai berikut:
```json
{
  "id":"id record",
  "name": "Nama Rumah Sakit",
  "address": "Alamat Rumah Sakit",
  "bedAvailable": "Jumlah Tempat Tidur yang available untuk pasien baru ",
  "queue": "Jumlah antrian tempat tidur ",
  "hotline": "Nomor Telpon rumah sakit",
  "updatedAt": {
   "hour": "Jam terakhir diupdate",
   "minute": "Menit terakhir diupdate"
  },
  "links": "Link detail data rumah sakit",
  "provinceId": "Id Provinsi"
  }
```

## Data Storing

1. ### Connect to MongoDB Atlas using MongoDB Compass
<img src="./Data Storing/screenshot/1.png"/>

2. ### Create collection
<img src="./Data Storing/screenshot/2.png"/>

3. ### Import JSON Data
<img src="./Data Storing/screenshot/3.png"/>

4. ### Hasil Import
<img src="./Data Storing/screenshot/6.png"/>

5. ### MongoDB Atlas
<img src="./Data Storing/screenshot/5.png"/>


__Connect MongoDB Compass to MongoDB Atlas:__ 
```
mongodb+srv://cabasdat:cabasdat@cluster0.j8w66.mongodb.net/test?authSource=admin&replicaSet=atlas-nihsut-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true
```
## API
Api yang dibuat menggunakan Bahasa pemrograman Go dengan menggunakan Framework ``Gin``. 
Link deployment, dapat diakses pada web berikut:
```url
https://hospital-web-ina.herokuapp.com
```
Untuk melakukan test terhadap API saya menggunakan [Isomnia](https://insomnia.rest/), karena tampilannya lebih user friendly dibanding Postman API

Untuk menjalankan di localhost:

#### __Menggunakan Docker__ 

1. Run command pada terminal
```cmd
cd "API/src
```
2. Jalankan Docker pada OS
3. Run command pada terminal
```cmd
docker-compose up
```
4. API akan diserve pada localhost:4747
5. Jika sudah exit dengan 
```cmd
CTRL + C
```
dan juga run command
```cmd
docker-compose down
```
#### __Tanpa Docker__ 
1. Run command pada terminal
```cmd
cd "Data Scraping/src
```
2. Run command
```cmd
go mod download
```
3.Run command
```cmd
go run main.go db.go type.go
```
4. API akan diserve pada localhost:4747
5. Jika sudah exit dengan 
```cmd
CTRL + C
```

#### API Endpoint
  __GET Method__
- Get All Hospitals
```url
https://hospital-web-ina.herokuapp.com/hospital
```
Responds Success

<img src="./api/screenshot/1.png"/>
- 
  - Get Hospital By Id
```url
https://hospital-web-ina.herokuapp.com/hospital/:id
```
Responds Success

Pada contoh ini menggunakan id ="a42b1666-3f08-44b6-b4d4-8d45d76490d7" yang di dapat dari endpoint create record yang ada di bawah

<img src="./api/screenshot/2.png"/>

  - Get List Provinces : Mereturn nama dan id provinsi yang dapat digunakan pada pencarian rumah sakit berdasarkan provinsi
```url
https://hospital-web-ina.herokuapp.com/province
```
Responds Success

<img src="./api/screenshot/3.png"/>

  - Get Hospital By Province 
```url
https://hospital-web-ina.herokuapp.com/province/:id
```
Responds Success : Pada request ini diberikan id=11 yang merupakan provinsi Aceh sehingga valid

<img src="./api/screenshot/4.png"/>

Responds Failed : Pada request ini diberikan id=5 yang tidak valid

<img src="./api/screenshot/5.png"/>

  __POST Method__

  - Create Hospital
```url
https://hospital-web-ina.herokuapp.com/hospital
```

Responds Success
Params: Body memiliki structure yang seperti ini

```json
{
    "name":"RS DR Rahmat",
    "address":"JL.",
    "bedAvailable":0,
    "queue":0,
    "hotline":"hotline tidak ada",
    "links":"http",
    "provinceId":11
}
```
ID yang digenerate, yaitu _"a42b1666-3f08-44b6-b4d4-8d45d76490d7"_ akan digunakan sepanjang tutorial ini
<img src="./api/screenshot/6.png"/>

__PATCH Method__

  - Update Hospital
```url
https://hospital-web-ina.herokuapp.com/hospital/:id
```

Responds Success
Params: Body memiliki structure yang seperti ini

```json
{
    "bedAvailable":1000,
    "provinceId":11
}
```
ID yang digunakan, yaitu _"a42b1666-3f08-44b6-b4d4-8d45d76490d7"_
<img src="./api/screenshot/7.png"/>

Saat Di get kembali sudah terupdate recordnya
<img src="./api/screenshot/8.png"/>

__PATCH Method__

  - Delete Hospital
```url
https://hospital-web-ina.herokuapp.com/hospital/:id
```

Responds Success

ID yang digunakan, yaitu _"a42b1666-3f08-44b6-b4d4-8d45d76490d7"_
<img src="./api/screenshot/9.png"/>

Saat Di get kembali record sudah terdelete
<img src="./api/screenshot/10.png"/>


## Reference(s)
### Library Used:
- gin
- colly
- mongodriver

### Tools:
- MongoDB Compass
- MongoDB Atlas
- Insomnia
- Docker
- Go Programming Language

-  [Colly Simple Example](http://go-colly.org/)
-  [Colly API Reference](https://pkg.go.dev/github.com/gocolly/colly)
-  [Gin API Reference](https://pkg.go.dev/github.com/gin-gonic/gin)
-  [Gin Rest With MongoDB Tutorial](https://medium.com/@cavdy/creating-restful-api-using-golang-and-mongodb-7f6abd4394eb)
 


## Author

```
Rahmat Wibowo
18219040
```

