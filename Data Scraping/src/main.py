#################################################LIBRARY YANG DIGUNAKAN##################################################

from bs4 import BeautifulSoup as bs
import requests
import os
import json
import pandas as pd

################################################VARIABEL GLOBAL##########################################################
objectArray = []    # array yang akan digunakan untuk menyimpan object dictionary berisi data mobil bekas
savepath = "D:/Kuliah/Seleksi-2021-Tugas-1/Data Scraping/data/"     # Lokasi penyimpanan data

###############################################FUNGSI / PROSEDUR#########################################################
def format_distance(distance):

    # Fungsi ini melakukan formatting terhadap data jarak tempuh yang dimiliki oleh tiap mobil
    # Secara umum, terdapat 2 buah format yang digunakan pada website https://www.mobil123.com
    # Format yang pertama adalah penulisan jarak tempuh secara langsung (e.g. 12345 KM)
    # Format yang kedua adalah penulisan jarak tempuh dalam bentuk rentang (e.g. 10 - 15K KM atau 10000 - 15000 KM)

    # Pada fungsi ini, saya melakukan standarisasi terhadap format jarak tempuh, sehingga jarak tempuh akan memiliki rentang data yang terbatas
    # Rentang data yang saya gunakan adalah sebagai berikut (dalam satuan KM).
        # 1. 0 - 10000
        # 2. 10000 - 25000
        # 3. 25000 - 50000
        # 4. 50000 - 75000
        # 5. 75000 - 100000
        # 6. 100000 - 150000
    # Pada web scraping yang saya lakukan, saya membatasi jarak tempuh maksimal suatu mobil adalah 150000 KM, dengan asumsi
    # bahwa semua mobil yang memiliki jarak tempuh > 150000 KM sudah terlalu sering digunakan dan kelayakan pakainya tidak terjamin.

    # Melakukan formatting pada data jarak tempuh yang memiliki format penulisan jarak tempuh secara langsung
    if("-" not in distance):
        if(len(distance) <= 7):     # data jarak tempuh berada pada kisaran nilai satuan - satuan ribu
            distance = "0 - 10000"
        elif(7 < len(distance) < 9):    # data jarak tempuh berada pada kisaran nilai puluhan ribu
            filter_numerik = filter(str.isdigit, distance)  # Mengambil alphabet yang merupakan digit(0-9) saja pada string
            distance = "".join(filter_numerik) # dan disimpan kembali pada variabel menjadi sebuah string
            jarak = int(distance)   # konversi string -> int
            if(jarak <= 25000):
                distance = "10000 - 25000"
            elif(25000 < jarak <= 50000):
                distance = "25000 - 50000"
            elif(50000 < jarak <= 75000):
                distance = "50000 - 75000"
            elif(75000 < jarak <= 100000):
                distance = "75000 - 100000"
        elif(len(distance) == 9):   # data jarak tempuh berada pada kisaran nilai ratusan ribu
            filter_numerik = filter(str.isdigit, distance)  # Mengambil alphabet yang merupakan digit(0-9) saja pada string
            distance = "".join(filter_numerik)      # dan disimpan kembali pada variabel menjadi sebuah string
            jarak = int(distance)       # konversi string -> int
            if(jarak <= 150000):
                distance = "100000 - 150000"
            else:
                distance = ""       # Saat jarak tempuh bernilai > 150000 KM, variabel distance akan berisi string kosong saja
        else:
            distance = ""       #panjang distance adalah >= 10, yang menandakan nilai variabel distance pada kisaran jutaan KM.

    # Melakukan formatting pada data jarak tempuh yang memiliki format penulisan dalam rentang
    else:
        if(distance == "0 - 5000 KM" or distance == "0 - 5000K KM" or 9 <= len(distance) <= 10):       # jarak tempuh dalam format satuan - ribuan, ribuan - ribuan, atau ribuan - puluhan ribu (e.g. 0 - 5K KM, 3 - 5K KM, 5 - 10K KM)
            distance = "0 - 10000"
        elif(11 <= len(distance) <= 18):
            distance = distance.replace(" KM", "")  # Menghapus " KM" dalam string
            if("K" in distance):
                distance = distance.replace("K", "")    # Menghapus "K" jika ada dalam string
            if(len(distance) == 7):     # jarak tempuh dalam format puluhan - puluhan (e.g. "25 - 30")
                batas_akhir = distance[5:7]     # Mengambil nilai batas atas dalam string (e.g. "25 - 30", maka "30" akan diambil)
                if(int(batas_akhir) <= 25):
                    distance = "10000 - 25000"
                elif(int(batas_akhir) <= 50):
                    distance = "25000 - 50000"
                elif(int(batas_akhir) <= 75):
                    distance = "50000 - 75000"
                elif(int(batas_akhir) < 100):
                    distance = "75000 - 100000"

            elif(len(distance) == 8):   # Jarak tempuh dalam format puluhan - ratusan (e.g. "95 - 100")
                batas_akhir = distance[5:8] # Mengambil nilai batas atas dalam string (e.g. "95 - 100", maka "100" akan diambil)
                if(int(batas_akhir) <= 100):
                    distance = "75000 - 100000"
                else:
                    distance = "100000 - 150000"

            elif(len(distance) == 9):   # Jarak tempuh dalam format ratusan - ratusan (e.g. "125 - 130")
                batas_akhir = distance[6:9] # Mengambil nilai batas atas dalam string (e.g. "100 - 105", maka "105" akan diambil)
                if(int(batas_akhir) <= 150):
                    distance = "100000 - 150000"
                else:
                    distance = ""

            elif(len(distance) == 12):      # Jarak tempuh dalam format ribuan - ribuan (e.g. 5000 - 10000)
                batas_akhir = distance[7:12] # Mengambil nilai batas atas dalam string (e.g. "5000 - 10000", maka "10000" akan diambil)
                if(int(batas_akhir) <= 10000):
                    distance = "0 - 10000"
                else:
                    distance = "10000 - 25000"
            elif(len(distance) == 13):      # Jarak tempuh dalam format puluhan ribu - puluhan ribu (e.g 15000 - 20000)
                batas_akhir = distance[8:13]    # Mengambil nilai batas atas dalam string
                if(int(batas_akhir) <= 25000):
                    distance = "10000 - 25000"
                elif(int(batas_akhir) <= 50000):
                    distance = "25000 - 50000"
                elif(int(batas_akhir) <= 50000):
                    distance = "25000 - 50000"
                elif(int(batas_akhir) <= 75000):
                    distance = "50000 - 75000"
                elif(int(batas_akhir) <= 100000):
                    distance = "75000 - 100000"
            elif(len(distance) == 14):      # Jarak tempuh dalam format puluhan ribu - ratusan ribu (e.g 95000 - 100000)
                batas_akhir = distance[8:14]    # Mengambil nilai batas atas dalam string
                if(int(batas_akhir) <= 100000):
                    distance = "75000 - 100000"
                else:
                    distance = "100000 - 150000"
            elif(len(distance) == 15):      # Jarak tempuh dalam format ratusan ribu - ratusan ribu (e.g 105000 - 110000)
                batas_akhir = distance[9:15]    # Mengambil nilai batas atas dalam string
                if(int(batas_akhir) <= 150000):
                    distance = "100000 - 150000"
                else:
                    distance = ""       # Jika int(batas_akhir) > 150000, maka nilai distance adalah empty string
        else:
            distance = ""       #Panjang string distance melebihi 18, sehingga distance akan diisi empty string
    return distance

def get_mobil_data(url):
    # Mengambil data mobil dari url yang diberikan
        response = requests.get(url)    # Menggunakan library requests untuk mengirimkan GET Request kepada url yang dimaksud
        html = response.content         # response.content akan mengambil data HTML dari url yang dituju
        soup = bs(html, "lxml")         # Data tersebut akan kita scraping menggunakan library BeautifulSoup (dalam hal ini saya beri nama bs)
                                        # Kita dapat melakukan inisiasi library ini dengan menuliskan bs() yang meminta 2 buah argumen, yaitu data HTML yang akan kita scrape
                                        # dan tipe parser yang akan digunakan. Disini, saya menggunakan "lxml" sebagai parser

        cars = soup.find_all("article", class_ = "listing")     # Masing-masing mobil dan info-infonya tersimpan pada sebuah elemen HTML "article"
                                                                # dan memiliki kelas "listing"
                                                                # Dengan metode soup.find_all(), akan mengembalikan sebuah array yang berisi
                                                                # masing-masing mobil dan infonya
                                                                # Jika tidak ditemukan elemen yang sesuai kriteria, maka akan mengembalikan array kosong
        for car in cars:    # traversing pada array tersebut
                harga_div = car.findAll("div", class_= "listing__price delta weight--bold")     # Pada elemen article masing-masing, kita dapat menemukan
                                                                                                # nilai harga mobil pada sebuah elemen "div" yang memiliki kelas "listing__price delta weight--bold"
                if(harga_div == []):
                    continue        # Jika pada article tersebut tidak ditemukan div yang dimaksud, maka loop akan langsung melakukan proses pada elemen selanjutnya
                else:
                    harga = harga_div[0].text.strip().replace("Rp ", "")    # Mengambil nilai harga mobil dan menambahkan metode strip() untuk menghilangkan whitespace kiri dan kanan elemen
                                                                            # metode .replace("Rp ","") mengganti string "Rp " -> empty string
                                                                            # Harga dalam satuan Rupiah(Rp)

                    data_tipe_mobil_tahun = car["data-display-title"]       #Kita dapat mengambil tahun dan tipe masing-masing mobil pada nilai atribut "data-display-title" pada elemen "article" masing-masing mobil
                                                                            # Struktur string ini adalah "Tahun" + "Tipe Mobil" (e.g. "2018 Toyota Hiace 2.5 High Grade Commuter Van")
                    tipe_mobil = data_tipe_mobil_tahun[5:]      # Mengambil data tipe mobil dari data_tipe_mobil_tahun

                    tahun = data_tipe_mobil_tahun[:4]           # Mengambil data tahun mobil dari data_tipe_mobil_tahun

                    car_km_div = car.findAll("div", class_ = "item push-quarter--ends soft--right push-quarter--right")     # Mengambil elemen yang memiliki nilai jarak tempuh dari mobil
                                                                                                                            # Elemen tersebut adalah "div" yang memiliki kelas "item push-quarter--ends soft--right push-quarter--right"
                    jarak_tempuh = car_km_div[0].text.strip().upper()   # Mengambil string jarak tempuh yang tersimpan pada car_km_div, dan mengaplikasikan fungsi strip() dan upper()
                                                                        # Jarak tempuh dalam satuan Kilometer(KM)

                    jarak_tempuh = format_distance(jarak_tempuh)        # Memanggil fungsi format_distance(jarak_tempuh)
                    if(jarak_tempuh == ""):
                        continue                                        # Jika jarak_tempuh bernilai empty string, maka loop akan langsung melakukan proses elemen selanjutnya

                    div_transmisi_lokasi = car.findAll("div", class_ = "item push-quarter--ends")       # informasi terkait jenis transmisi dan lokasi penjualan terkandung dalam sebuah elemen yang sama
                                                                                                        # yaitu sebuah div yang memiliki kelas "item push-quarter--ends"

                    transmisi = div_transmisi_lokasi[0].text.strip()    # Mengambil informasi jenis transmisi dari div

                    lokasi_penjualan = div_transmisi_lokasi[1].text.strip()     # Mengambil informasi lokasi penjualan dari div

                    tipe_penjual_div = car.findAll("div", class_= "item push-quarter--ends listing__spec--dealer")      # Mencari elemen div yang memiliki kelas "item push-quarter--ends listing__spec--dealer"
                    tipe_penjual = tipe_penjual_div[0].text.strip().replace(" ", "").split()[0]         # Mengambil informasi jenis penjual masing- masing mobil
                    # print(tipe_penjual)       #Uncomment dan jalankan kode ini untuk mengetahui nilai tipe_penjual
                                                # Pada titik ini, terdapat kurang lebih 3 jenis nilai tipe_penjual, yaitu Dealer, SalesAgent, dan Private
                    if(tipe_penjual == "SalesAgent"):
                        tipe_penjual = "Sales Agent"     # Memisahkan SalesAgent menjadi Sales Agent

                    scrapeRecord = {                    #dictionary yang menyimpan data tiap mobil
                    "TipeMobil"      : tipe_mobil,
                    "Tahun"          : tahun,
                    "Harga"          : harga,
                    "Jarak"          : jarak_tempuh,
                    "Transmisi"      : transmisi,
                    "Lokasi"         : lokasi_penjualan,
                    "Penjual"        : tipe_penjual
                    }

                    objectArray.append(scrapeRecord)    #Menambahkan scrapeRecord ke objectArray


def scraper_mobil_bekas():
    # Melakukan scraping untuk mengambil data mobil bekas, dan menyimpannya dalam sebuah file .json
    page = 1
    print("Nama File? (tidak perlu menambahkan format .json, cukup namanya saja)")
    filename = input("> ")      # Nama file .json
    if(".json" in filename.lower()):
        filename = filename.replace(".json", "")
    while(page != 201):         # Proses dilakukan pada 200 halaman, dengan tiap halaman terdapat kurang lebih 25 mobil yang ditawarkan
        url = f"https://www.mobil123.com/mobil-dijual/indonesia?type=used&page_number={page}"       # url yang dituju
        get_mobil_data(url)     # Memanggil fungsi get_mobil_data(url)
        page += 1               #traversing

    dumper = json.dumps(objectArray, indent=4)      # Melakukan dumping pada array objectArray yang berisi sekumpulan dictionary.
                                                    # indent=4 digunakan untuk mengatur indentasi object pada file .json yang akan dihasilkan
    filepath = os.path.join(savepath, filename + ".json")
    with open(filepath, "w") as file:
        file.write(dumper)      # Memanggil fungsi open() untuk menuliskan data dumper pada file bernama (filename + ".json")
        file.close()            # Menutup fungsi open()
        print("\nThe scraped data is saved to data/" + filename + ".json")       # Menampilkan pesan bahwa data scraping telah disimpan pada file .json terkait
        print("Saved " + str(len(objectArray)) + " datas")

def get_JSON_data(filename):
    # Menampilkan data yang terdapat pada filename.json
    filepath = os.path.join(savepath, filename + ".json")
    file = open(filepath, "r")

    items = json.load(file)

    for item in items:
        print(item)

    file.close()

def get_JSON_dataframe(filename):
    # menampilkan data yang terdapat pada filename.json secara dataframe menggunakan bantuan library pandas
    df = pd.read_json(filename + ".json")
    print(df)

###############################################IMPLEMENTASI################################################################
scraper_mobil_bekas()
