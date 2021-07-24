import requests
import time
import os
from datetime import datetime, date, timedelta

import json
from bs4 import BeautifulSoup

# header
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) \
AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 \
Safari/537.2'}

# url billboard
baseURL = 'https://www.billboard.com/charts'

# min available chart week
minWeek = {
    'hot-100': date(1958, 8, 9),
    'artist-100': date(2014, 7, 26),
    'billboard-200': date(1963, 8, 24)
}

# find all week
def findAllWeek(year):
    # allWeek = []
    d = date(year, 1, 1)             # January 1st
    d += timedelta(days = (5 - d.weekday() + 7) % 7)     # First saturday
    while d.year == year:
        yield d
        #allWeek.append(d)
        d += timedelta(days = 7)

# find current week
def findCurrentWeek():
    d = date.today()
    d += timedelta(days = (5 - d.weekday() + 7) % 7)
    return d

# find all previos week from a spesific year
def findAllPreviousWeek(year):
    weeks = []
    currentWeek = findCurrentWeek()
    for w in findAllWeek(year):
        weeks.append(w)
        if (w==currentWeek):
            break
    return weeks

def findAllAvailableWeek(chartType, minYear, maxYear):
    weeks = []
    for i in range(minYear, maxYear+1):
        for w in findAllPreviousWeek(i):
            if (w >= minWeek[chartType]):
                weeks.append(w)
    return weeks

# find all week which not exist as json file
def findAllNotExistWeek(chartType, weeks):
    notExistWeeks = []
    for w in weeks:
        if (not isFileExist(chartType, w)):
            notExistWeeks.append(w)
    return notExistWeeks


# convert format date string M D, Y to Y-M-D
def strToYMD(d):
    return datetime.strptime(d, '%B %d, %Y').strftime('%Y-%m-%d')

def strToDate(d):
    return datetime.strptime(d, '%Y-%m-%d')

def dateToStr(d):
    return d.strftime('%Y-%m-%d')

def dateTimeToStr(d):
    return d.strftime('%Y-%m-%d %H:%M:%S')

# convert string 'None' to Nonetype
def strToNone(string):
    if (string == 'None') :
        return None
    return string

def strToNumeric(string):
    if (string.isnumeric()):
        return int(string)
    return string

def convertToOriginType(var):
    return strToNone(strToNumeric(var))

def replacedAllSubStr(string, listSubStr, subStrToBe):
    for char in listSubStr:
        string = string.replace(char, subStrToBe)
    return string

# check if a spesific json file exist
def isFileExist(chartType, chartWeek):
    return os.path.isfile(f'Data Scraping/data/{chartType}/{chartWeek.year}/{chartWeek}.json')

def setDataDict(chart_week):
    return {
        'fetchTime': dateTimeToStr(datetime.now()),
        'chartWeek': chart_week,
        'chart': []
    }

def inputYear(str):
    while True:
        inputStr = input(str)
        if (inputStr.isnumeric()):
            break
    return int(inputStr)


def getHot100Chart(week):
    chartType = 'hot-100'

    source = requests.get(baseURL+'/'+chartType+'/'+dateToStr(week), headers=header).text
    soup = BeautifulSoup(source, 'html.parser')
    chart_week = soup.find('button', class_='date-selector__button button--link').text.strip()
    chart_week = strToYMD(chart_week)
    chart_data = setDataDict(chart_week)
    chart_list = soup.find_all('li', class_='chart-list__element display--flex')

    for chart_element in chart_list:
        number = chart_element.find('span', class_='chart-element__rank__number').text
        title = chart_element.find('span', class_='chart-element__information__song text--truncate color--primary').text
        artist = chart_element.find('span', class_='chart-element__information__artist text--truncate color--secondary').text.strip()
        replacedStr = [' Featuring ', ' & ', ' (', ' + ', ' X ', ' With ', ' x ', ' Feat. ']
        artist_list = replacedAllSubStr(artist, replacedStr, ', ')
        artist_list = artist_list.replace(')', '').split(', ')
        last_week = chart_element.find('span', class_='chart-element__meta text--center color--secondary text--last').text.replace('-','None')
        peak = chart_element.find('span', class_='chart-element__meta text--center color--secondary text--peak').text.replace('-','None')
        week_on_chart = chart_element.find('span', class_='chart-element__meta text--center color--secondary text--week').text.replace('-','None')

        chart_data['chart'].append({
            'rank': convertToOriginType(number),
            'title': title,
            'artist': artist,
            'listArtist': artist_list,
            'lastWeek': convertToOriginType(last_week),
            'peakRank': convertToOriginType(peak),
            'weekOnChart': convertToOriginType(week_on_chart)
        })

    json_object = json.dumps(chart_data, indent = 4)
    filename = f'Data Scraping/data/{chartType}/{strToDate(chart_week).year}/{chart_week}.json'
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as outfile:
        outfile.write(json_object)
    print(f'File saved: {filename}')

def getArtist100Chart(week):
    chartType = 'artist-100'
    
    source = requests.get(baseURL+'/'+chartType+'/'+dateToStr(week), headers=header).text
    soup = BeautifulSoup(source, "html.parser")
    chart_week = soup.find('button', class_='chart-detail-header__date-selector-button').text.strip()
    chart_week = strToYMD(chart_week)

    chart_data = setDataDict(chart_week)


    chart_list = soup.find_all('div', class_='chart-list-item')
    for chart_element in chart_list:
        number = chart_element['data-rank']
        artist = chart_element['data-title']
        last_week = chart_element.find('div', class_='chart-list-item__last-week').text.replace('-','None')
        peak = chart_element.find('div', class_='chart-list-item__weeks-at-one').text.replace('-','None')
        weeks_on_chart = chart_element.find('div', class_='chart-list-item__weeks-on-chart').text.replace('-','None')
        labels = chart_element.find('div', class_='chart-list-item__people_data-cell').text.replace('Imprint/Promotion Label:','').strip().split(' | ')

        chart_data['chart'].append({
            'rank': convertToOriginType(number),
            'artist': artist,
            'lastWeek': convertToOriginType(last_week),
            'peakRank': convertToOriginType(peak),
            'weekOnChart': convertToOriginType(weeks_on_chart),
            'label': labels
        })

    json_object = json.dumps(chart_data, indent = 4)
    filename = f'Data Scraping/data/{chartType}/{strToDate(chart_week).year}/{chart_week}.json'
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as outfile:
        outfile.write(json_object)

    print(f'File saved: {filename}')

def getBillboard200Chart(week):
    chartType = 'billboard-200'

    source = requests.get(baseURL+'/'+chartType+'/'+dateToStr(week), headers=header).text
    soup = BeautifulSoup(source, 'html.parser')
    chart_week = soup.find('button', class_='date-selector__button button--link').text.strip()
    chart_week = strToYMD(chart_week)
    chart_data = setDataDict(chart_week)
    chart_list = soup.find_all('li', class_='chart-list__element display--flex')
    for chart_element in chart_list:
        number = chart_element.find('span', class_='chart-element__rank__number').text
        title = chart_element.find('span', class_='chart-element__information__song text--truncate color--primary').text
        artist = chart_element.find('span', class_='chart-element__information__artist text--truncate color--secondary').text.strip()
        replacedStr = [' Featuring ', ' & ', ' (', ' + ', ' X ', ' With ', ' x ', ' Feat. ']
        artist_list = replacedAllSubStr(artist, replacedStr, ', ')
        artist_list = artist_list.replace(')', '').split(', ')
        last_week = chart_element.find('span', class_='chart-element__meta text--center color--secondary text--last').text.replace('-','None')
        peak = chart_element.find('span', class_='chart-element__meta text--center color--secondary text--peak').text.replace('-','None')
        week_on_chart = chart_element.find('span', class_='chart-element__meta text--center color--secondary text--week').text.replace('-','None')

        chart_data['chart'].append({
            'rank': convertToOriginType(number),
            'title': title,
            'artist': artist,
            'listArtist': artist_list,
            'lastWeek': convertToOriginType(last_week),
            'peakRank': convertToOriginType(peak),
            'weekOnChart': convertToOriginType(week_on_chart)
        })

    json_object = json.dumps(chart_data, indent = 4)
    filename = f'Data Scraping/data/{chartType}/{strToDate(chart_week).year}/{chart_week}.json'
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as outfile:
        outfile.write(json_object)

    print(f'File saved: {filename}')


# main 
if __name__ == '__main__':
    print("Billboard Chart Web Scrapper")

    while True :
        print("Pilih Billboard chart yang akan di-scrape:")
        print("1. The Hot 100")
        print("2. Artist 100")
        print("3. Billboard 200")
        print("0. Exit")
        inputChart = input('>')
        print()
        if (inputChart=='1'):
            minYear = minWeek['hot-100'].year
            print ("Catatan : The Hot 100 tersedia mulai tahun {}".format(minYear))
            startYear = inputYear("Masukkan range tahun awal: ")
            endYear = inputYear("Masukkan range tahun akhir: ")
            startYear = max(startYear, minYear)
            endYear = min(endYear, datetime.now().year)

            weekList = findAllNotExistWeek('hot-100', findAllAvailableWeek('hot-100', startYear, endYear))

            print(f"Scrape The Hot 100 dari {startYear} sampai {endYear}")
            for week in weekList:
                getHot100Chart(week)
                time.sleep(2)

        elif (inputChart=='2'):
            minYear = minWeek['artist-100'].year
            print ("Catatan : Artist 100 tersedia mulai tahun {}".format(minYear))
            startYear = inputYear("Masukkan range tahun awal: ")
            endYear = inputYear("Masukkan range tahun akhir: ")
            startYear = max(startYear, minYear)
            endYear = min(endYear, datetime.now().year)

            weekList = findAllNotExistWeek('artist-100', findAllAvailableWeek('artist-100', startYear, endYear))

            print(f"Scrape Artist 100 dari {startYear} sampai {endYear}")
            for week in weekList:
                getArtist100Chart(week)
                time.sleep(2)

        elif (inputChart=='3'):
            minYear = minWeek['billboard-200'].year
            print ("Catatan : Billboard 200 tersedia mulai tahun {}".format(minYear))
            startYear = inputYear("Masukkan range tahun awal: ")
            endYear = inputYear("Masukkan range tahun akhir: ")
            startYear = max(startYear, minYear)
            endYear = min(endYear, datetime.now().year)

            weekList = findAllNotExistWeek('billboard-200', findAllAvailableWeek('billboard-200', startYear, endYear))

            print(f"Scrape Billboard 200 dari {startYear} sampai {endYear}")
            for week in weekList:
                getBillboard200Chart(week)
                time.sleep(2)

        elif (inputChart=='0'):
            print("Terimakasih telah menggunakan scrapper ini!")
            break

        else:
            print("Masukkan input yang sesuai!")
            inputChart = input('>')