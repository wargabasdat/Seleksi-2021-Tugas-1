import requests
import json
from bs4 import BeautifulSoup
import pymongo


def setupDatabase():
    db = pymongo.MongoClient(
        "mongodb+srv://dwibagus154:mUnvBeu7vR3hAaK@cluster0.uqmyh.mongodb.net/test?retryWrites=true&w=majority")

    # database
    mydatabase = db["scraping"]
    # collection
    collection = mydatabase['imdb']
    return collection


def setupUrl(page):
    url = 'https://www.imdb.com/search/keyword/?keywords=action-hero&ref_=kw_nxt&sort=moviemeter,asc&mode=detail&page=' + \
        str(page)

    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'html.parser')

    items = soup.findAll('div', 'lister-item mode-detail')

    return items


def pecahString(strings):
    # membuat string menjadi lebih bagus
    new = ''
    for i in range(1, len(strings)):
        new += strings[i]
        if strings[i] == " " and strings[i+1] == " " and strings[i+2] == " ":
            break
    return new


def scrapProgram(data, items, collection):
    # data = []
    for item in items:
        title = item.find('h3', 'lister-item-header').find('a').text
        description = pecahString(item.find('p', '').text)
        # dalam film mungkinada yang tidak ada rating, time, ataupun certificate
        rating = None
        time = None
        certificate = None
        if item.find('div', 'inline-block ratings-imdb-rating') != None:
            rating = float(item.find(
                'div', 'inline-block ratings-imdb-rating').find('strong').text)
        temps = item.findAll('p', 'text-muted text-small')
        genre = pecahString(temps[0].find('span', 'genre').text)

        if temps[0].find('span', 'runtime') != None:
            time = pecahString(temps[0].find('span', 'runtime').text)
        if temps[0].find('span', 'certificate') != None:
            certificate = temps[0].find('span', 'certificate').text
#
        dummy = {
            'title': title,
            'description': description,
            'rating': rating,
            'genre': genre,
            'time': time,
            'certificate': certificate
        }
        dummy1 = {
            'title': title,
            'description': description,
            'rating': rating,
            'genre': genre,
            'time': time,
            'certificate': certificate
        }
        collection.insert_one(dummy1)
        data.append(dummy)
    return data


def createJSONfile(data):
    with open('./Data Scraping/data/data.json', 'w') as jsonfile:
        inputdata = {
            'massage': 'https://www.imdb.com/search/keyword/?keywords=action-hero&ref_=kw_nxt&sort=moviemeter,asc&mode=detail&page=1',
            'data': data
        }
        json.dump(inputdata, jsonfile)


def mainProgram():
    collection = setupDatabase()
    data = []
    jumlahPage = 20
    for i in range(1, jumlahPage+1):
        items = setupUrl(i)
        data = scrapProgram(data, items, collection)
    createJSONfile(data)
    # print(data), #uncomment comment ini untuk mengecek data yang dihasilkan di terminal


mainProgram()
