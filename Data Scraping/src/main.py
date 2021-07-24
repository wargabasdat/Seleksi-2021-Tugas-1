# Jacelyn Felisha
# 18219097
# Sistem dan Teknologi Informasi

# library yang digunakan
import json
import time
import requests
from bs4 import BeautifulSoup

# ganti path sesuai direktori data.json 
path = "D:\Jacelyn\Lab-Basdat\seleksi-1\Data Scraping\data\data.json"

# fungsi untuk meng-export data ke format json 
# source: https://www.geeksforgeeks.org/append-to-json-file-using-python/
def write_to_json(data, filename=path):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["restaurants"].append(data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

# fungsi untuk scraping data dari halaman web yang diinginkan
def get_restaurants_data(page_number):
    url = "https://pergikuliner.com/restaurants?default_search=Jakarta&page=" + str(page_number) + "&search_name_cuisine=&search_place="

    # headers dapat diganti sesuai user agent yang ingin digunakan
    headers = {'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64); Basis Data/Admin Basis Data/basisdata@std.stei.itb.ac.id'}
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    restaurants = soup.find_all('div', class_='restaurant-result-wrapper')
    arr_new_data = []
    id = ((page_number-1)*12)+1

    for restaurant in restaurants:
        # mengambil data lebih lengkap dari url dalam url awal
        spesific_url = "https://pergikuliner.com" + restaurant.h3.a["href"]
        spesific_page = requests.get(spesific_url, headers=headers)
        spesific_soup = BeautifulSoup(spesific_page.content, 'html.parser')
        info_list = spesific_soup.find("div", class_="info-list").find_all("li")

        arr_pembayaran = []
        for info in info_list:
            if("Pembayaran" in info.text):
                if(',' in info.meta["content"]):
                    arr_pembayaran = info.meta["content"].split(',')
                else:
                    arr_pembayaran.append(info.meta["content"])

        cabang_final = False
        for info in info_list:
            if("Cabang" in info.text):
                cabang_final = True

        fasilitas_list = spesific_soup.find("div", class_="facility-list").find_all("li")
        arr_fasilitas = []
        for fasilitas in fasilitas_list:
            if(fasilitas.find("label", class_="checked")):
                arr_fasilitas.append(fasilitas.text.strip())

        nama = restaurant.h3.text

        alamat = restaurant.p.span.find_all('span', class_="truncate")[1].text
        daerah_cuisine = restaurant.find('div', class_='item-group').div.text
        arr_daerah_cuisine = daerah_cuisine.split(' | ')
        daerah = arr_daerah_cuisine[0]
        arr_cuisine = []
        if(len(arr_daerah_cuisine) > 1):
            cuisine = arr_daerah_cuisine[1]
            if(',' in cuisine):
                arr_cuisine = cuisine.strip().split(',')
            else:
                arr_cuisine.append(cuisine.strip())

        harga = restaurant.find_all('p', class_='clearfix')[1].text
        rating = restaurant.find('div', class_='item-rating-result').text.replace(' /5', '')
        
        # menyatukan data-data yang telah diambil menjadi suatu objek
        new_data = {"id": str(id),
            "nama": nama.strip(),
            "alamat": alamat.strip(),
            "daerah": daerah.strip(),
            "tipe kuliner": arr_cuisine,
            "kisaran harga": harga.strip(),
            "rating": float(rating.strip()),
            "pembayaran": arr_pembayaran,
            "cabang": cabang_final,
            "fasilitas": arr_fasilitas,
        }

        # menambahkan objek baru ke array restoran
        arr_new_data.append(new_data)
        id+=1
        
        # memberikan jeda waktu 10 detik saat pengambilan data dari satu restoran ke restoran lain
        time.sleep(10)
    
    # meng-export sekaligus menambahkan data restoran ke data.json
    for new_data in arr_new_data:
        write_to_json(new_data)
    print("New restaurants added to data.json(from url page " + str(page_number) + ")!")

# mengambil data restoran dari page 1 - 40 (480 restoran)
from_page = 1
until_page = 40
for i in range(from_page, until_page+1):
    get_restaurants_data(i)