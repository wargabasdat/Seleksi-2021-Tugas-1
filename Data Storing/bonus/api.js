// Inisiasi dan import library yang akan digunakan
const express = require("express");
const mongoose = require("mongoose");
const _ = require("lodash");

// Inisiasi API yang menggunakan framework Express.JS
const app = express();


// Menghubungkan API ke database yang digunakan, yaitu MongoDB Atlas, dengan alamat cluster, database, dan collection sebagai berikut
mongoose.connect("mongodb+srv://admin-baskoro:tes123@seleksibasdat.nbkkl.mongodb.net/mobil_bekas", {useNewUrlParser : true});

// Skema dari collection yang diakses, yaitu collection cars
const carSchema = {
    TipeMobil : String,
    Tahun : String,
    Harga : String,
    Jarak : String,
    Transmisi : String,
    Lokasi : String,
    Penjual : String
};

// Membuat model berdasarkan schema yang sudah didefinisikan
const Car = mongoose.model("Car", carSchema);

app.use(express.urlencoded({
    extended : true
}));

// alamat pencarian
// Cara mengakses setiap app.route -> ketikkan "localhost:3000/<routeYangDiinginkan>" (tanpa tanda petik)

app.route("/cars")
    // Mendapatkan seluruh data mobil bekas yang ada di collection
    .get((req, res) => {
        Car.find({}, (err, results) => {
            if(err){
                res.send(err);
            }
            else{
                res.send(results);
            }
        });
    });

app.route("/cars/jarak/min_length=:minMileage/max_length=:maxMileage")
    // Mendapatkan data mobil bekas berdasarkan rentang jarak tempuh yang diinginkan
    .get((req, res) => {
        // constraint min dan max Mileage hanya input tertentu saja, yaitu dibatasi pada 0, 10000, 25000, 50000, 75000, 100000, 150000
        const minMileage = req.params.minMileage;
        const maxMileage = req.params.maxMileage;
        const mileage = mileageValidator(minMileage, maxMileage);   // Nilai konstanta mileage diisi oleh nilai mileage dari fungsi mileageValidator()
        Car.find({Jarak : mileage}, (err, results) => {     // Mencari data pada collection dimana value dari key Jarak == nilai mileage
            if(err){
                res.send(err);
            }
            else{
                if(results.length !== 0){
                    res.send(results);
                }
                else{
                    res.send("Nothing was found...");
                }
            }
        });
    });

const mileageValidator = (minMileage, maxMileage) => {
    // Mendapatkan nilai sebuah variabel mileage sesuai format yang ditentukan dari input minMileage dan maxMileage
    let mileage;
    switch(intMin = parseInt(minMileage), intMax = parseInt(maxMileage)){
        case 0:
        case 10000:
        case 25000:
        case 50000:
        case 75000:
        case 100000:
        case 150000: // Pada kasus nilai == 0 hingga kasus nilai == 100000, semuanya fall-through mengikuti kode pada case 1500000
            if(intMin > intMax){
                let temp = minMileage;
                minMileage = maxMileage;
                maxMileage = temp;
            }
            mileage = minMileage + " - " + maxMileage;
            break;
    };
    return mileage;
};

app.route("/cars/year/:carYear")
    // Mendapatkan data dari mobil yang merupakan produk keluaran dari suatu tahun tertentu
    .get((req, res) => {
        const carYear = req.params.carYear;
        Car.find({Tahun : carYear}, (err, results) => {     // Mencari data pada collection dimana value dari key Tahun == nilai carYear
            if(err){
                res.send(err);
            }
            else{
                if(results){
                    res.send(results);
                }
                else{
                    res.send("Nothing was found...");
                }
            }
        });
    });

app.route("/cars/penjual/:penjual")
    // Menampilkan data dari mobil bekas yang memiliki tipe penjual tertentu
    // Terdapat 3 nilai penjual, yaitu Dealer, Sales Agent, dan Private
    .get((req, res) => {
        const tipePenjual = _.startCase(req.params.penjual);    //pada const tipePenjual, semua kata yang ada akan diawali oleh sebuah huruf kapital
        Car.find({Penjual : tipePenjual}, (err, results) => {   // Mencari data pada collection dimana value dari key Penjual == nilai tipePenjual
            if(err){
                res.send(err);
            }
            else{
                if(results){
                    res.send(results);
                }
                else{
                    res.send("Nothing was found...");
                }
            }
        });
    });

app.route("/cars/lokasi/:lokasi")
    // Menampilkan data dari mobil bekas yang dijual pada suatu provinsi tertentu saja
    .get((req, res) => {
        const lokasiJual = _.startCase(req.params.lokasi);
        Car.find({Lokasi : lokasiJual}, (err, results) => {   // Mencari data pada collection dimana value dari key Lokasi == nilai lokasiJual
            if(err){
                res.send(err);
                }
            else{
                if(results){
                    res.send(results);
                }
                else{
                    res.send("Nothing was found...");
                }
            }
        });
    });

app.route("/cars/transmisi/:transmission")
    // Menampilkan data mobil bekas yang memiliki transmisi tertentu saja
    .get((req, res) => {
        const transmission = _.startCase(req.params.transmission);
        Car.find({Transmisi : transmission}, (err, results) => {   // Mencari data pada collection dimana value dari key Transmisi == nilai transmission
            if(err){
                res.send(err);
            }
            else{
                if(results){
                    res.send(results);
                }
                else{
                    res.send("Nothing was found...");
                }
            }
        });
    });

app.route("/cars/harga/max_harga=:hargaJual")
    // Menampilkan data mobil bekas yang memiliki harga tidak lebih tinggi dari harga masukan pengguna
    .get((req, res) => {
        const harga = parseInt(req.params.hargaJual);
        Car.find({}, (err, results) => {
            if(err){
                res.send(err);
            }
            else{
                if(results.length !== 0){
                    const resultContainer = [];     // array penampung hasil
                    results.forEach((result) => {   // traversing pada results
                        let hargaMobil = result.Harga.replace(/[.]+/g,"");  // regex digunakan untuk mencocokkan karakter "." pada string, dan akan digunakan fungsi replace() untuk mengganti seluruh char "." yang ditemukan dengan empty string
                        hargaMobil = parseInt(hargaMobil);      // str -> int conversion
                        if(hargaMobil <= harga){
                            resultContainer.push(result);       // Jika harga dari mobil bekas tidak lebih tinggi dari harga masukan pengguna, data tersebut ditambahkan pada array penampung
                            console.log(hargaMobil);
                        }
                    })
                    res.send(resultContainer);      //Menampilkan data yang ada pada resultContainer
                }
            }
        })
    })

app.route("/cars/harga/min_harga=:hargaJual")
// Menampilkan data mobil bekas yang memiliki harga tidak lebih rendah dari harga masukan pengguna
// Secara umum sama seperti GET dengan max_harga
// Perbedaannya adalah pada GET ini, data mobil bekas yang ditampilkan memiliki harga tidak lebih rendah dari harga masukan pengguna
    .get((req, res) => {
        const harga = parseInt(req.params.hargaJual);
        Car.find({}, (err, results) => {
            if(err){
                res.send(err);
            }
            else{
                if(results.length !== 0){
                    const resultContainer = [];
                    results.forEach((result) => {
                        let hargaMobil = result.Harga.replace(/[.]+/g,"");
                        hargaMobil = parseInt(hargaMobil);
                        if(hargaMobil >= harga){
                            resultContainer.push(result);
                            console.log(hargaMobil);
                        };
                    });
                    res.send(resultContainer);
                };
            };
        });
    });

app.route("/cars/harga/min_harga=:batasBawah/max_harga=:batasAtas")
// Menampilkan data mobil bekas yang memiliki harga pada rentang min_harga-max_harga
    .get((req,res) => {
        const minHarga = req.params.batasBawah;
        const maxHarga = req.params.batasAtas;
        Car.find({}, (err, results) =>{
            if(err){
                res.send(err);
            }
            else{
                if(results.length !== 0){
                    const resultContainer = [];
                    results.forEach(result => {
                        let hargaMobil = result.Harga.replace(/[.]+/g,"");
                        hargaMobil = parseInt(hargaMobil);
                        if(hargaMobil >= minHarga && hargaMobil <= maxHarga){
                            resultContainer.push(result);
                            console.log(hargaMobil);
                        }
                    });
                    res.send(resultContainer);
                }
            }
        });
    });

app.route("/cars/brand/:brandName")
// Menampilkan data mobil bekas yang diproduksi oleh brand tertentu saja (e.g. Mercedes-Benz, Toyota, dll)
    .get((req, res) => {
        const brandName = req.params.brandName;
        Car.find({}, (err, results) => {    // Mengambil seluruh data collection
            if(err){
                res.send(err);
            }
            else{
                if(results.length !== 0){
                    const resultContainer = [];     // array penampung hasi;
                    results.forEach(result => {     // traversing results
                        const brand = _.startCase(_.lowerCase(result.TipeMobil));       // Pada pengecekan, semua value tipeMobil diformat menjadi Start Casing, yaitu huruf kapital pada karakter pertama tiap katanya
                        const brandRegex = new RegExp(_.startCase(brandName), "y");     // Brand masukan pengguna akan digunakan sebagai substring untuk pencocokan menggunakan regex
                        const res = brandRegex.test(brand);     // Melakukan pencocokan terhadap tipe mobil yang ada menggunakan regex
                        if(res){
                            resultContainer.push(result);       // Jika ditemukan kecocokan, maka data tersebut akan ditambahkan pada array resultContainer
                            console.log(brand);
                        }
                    });
                    res.send(resultContainer);      // Menampilkan array resultContainer sebagai hasilnya
                };
            };
        });
    });

// Aplikasi akan berjalan pada port 3000 menggunakan host localhost
// Untuk mengakses API, gunakan localhost:3000
app.listen(3000, () => console.log("Server started on port 3000"));