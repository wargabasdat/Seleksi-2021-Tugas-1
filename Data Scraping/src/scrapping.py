import requests
from bs4 import BeautifulSoup
import json
import unicodedata  # converting unicode to plain string

# Init var
clubs = []
players = []
headers = {'User-Agent':
           'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}
base_link = "https://www.transfermarkt.com"

basePage = base_link + "/liga-1-indonesia/startseite/wettbewerb/IN1L"
pageTree = requests.get(basePage, headers=headers)
pageSoup = BeautifulSoup(pageTree.content, 'lxml')
basePageContent = pageSoup.find("div", id="yw1")

# Get all club list
club_list = basePageContent.find("tbody")
club_list = club_list.find_all("tr")
for club in club_list:
    tdTag = club.find(
        "td", class_="hauptlink no-border-links show-for-small show-for-pad")
    clubDetail = (tdTag.find("a", class_="vereinprofil_tooltip", href=True))
    clubId = clubDetail['id']  # in html tag
    squad_link = clubDetail['href']

    # make new request for club detail page
    clubPage = requests.get(base_link + squad_link, headers=headers)
    pageSoup = BeautifulSoup(clubPage.content, 'lxml')
    # get club info part
    clubName = pageSoup.find("div", class_="dataName").find("h1").text.strip()
    stadiumName = pageSoup.find("a", id=clubId).text
    managerName = (pageSoup.find("a", id="0").text)
    managerName = unicodedata.normalize(
        'NFKD', managerName).encode('ascii', 'ignore').decode()
    newClubItem = {
        'name': clubName,
        'manager': managerName,
        'league': 'Liga 1 Indonesia',
        'stadium': stadiumName
    }
    clubs.append(newClubItem)
    print(clubName)

    # make new request for players
    squad_link = squad_link.replace("startseite", "kader")
    playerPage = requests.get(
        base_link + squad_link + "/plus/1", headers=headers)
    pageSoup = BeautifulSoup(playerPage.content, 'lxml')
    playerTable = pageSoup.find(
        "div", {"id": "yw1"}).find("tbody").find_all("tr", {"class": ["odd", "even"]})

    # Retrieve player data
    for player in playerTable:
        tableName = (player.find(
            "table", {"class": "inline-table"}).find_all("tr"))
        name = tableName[0].find(
            "td", {"class": "hauptlink"}).find("a")["title"]
        name = unicodedata.normalize('NFKD', name).encode(
            'ascii', 'ignore').decode()
        position = (player.find(
            "table", {"class": "inline-table"}).find_all("tr"))[1].find("td").text
        number = player.find("div", class_="rn_nummer").text
        base = player.find_all("td", {"class": "zentriert"})
        dateOfBirth = (base[1].text)
        dateOfBirth = dateOfBirth[:(len(dateOfBirth) - 5)].replace(",", "")
        nationality = base[2].find("img")['title']
        height = base[3].text.replace(",", "").replace("m", "")
        foot = base[4].text
        marketValue = player.find(
            "td", class_="rechts hauptlink").text.replace("Th.", "").replace(u'\xa0', u'').replace("€", "")

        # clean
        if(height[0] == " "):
            height = "-"

        # add new player item
        newPlayer = {
            "name": name,
            "number": (None if number == "-" else number),
            "position": (None if position == "-" else position),
            "date-of-birth": (None if dateOfBirth == "" else dateOfBirth),
            "nationality": (None if nationality == "-" else nationality),
            "height": (None if height == "-" else int(height)),
            "foot": (None if foot == "-" else foot),
            "market-value": (None if marketValue == "-" else int(marketValue)),
            "club": clubName
        }
        players.append(newPlayer)

# Creating json objects
data = {
    "data": {
        "clubs": clubs,
        "players": players
    }
}
# clubs = { 'clubs': clubs }
# players = {'players' : players}

# with open('../data/clubs.json', 'w') as fp:
#     json.dump(clubs, fp)
# with open('../data/players.json', 'w') as fp:
#     json.dump(players, fp)
with open('../data/scrap.json', 'w') as fp:
    json.dump(data, fp)