# Convert json file to dictionary
import json
import datetime
from logging import NullHandler
import mysql.connector as msql
from mysql.connector import Error
from decouple import config

HOST = config('HOST')
DB_USER = config('DB_USER')
DB_PASS = config('DB_PASS')
DB_NAME = config('DB_NAME')

# Load JSON file
with open('../../data/scrap.json') as json_file:
    data = json.load(json_file)['data']

queryClubs = '''INSERT INTO Clubs (name, manager, league, stadium) VALUES '''
queryPlayers = '''INSERT INTO Players (name, number, position, birthDate, nationality, height, foot, marketValue, clubId) VALUES '''
lenClub = len(data['clubs'])
lenPlayers = len(data['players'])

# INSERT CLUBS
for i in range(lenClub):
    club = data['clubs'][i]
    itemClub = f"(\'{club['name']}\',\'{club['manager']}\',\'{club['league']}\', \'{club['stadium']}\')"
    if(i != lenClub-1):
        itemClub += ','
    queryClubs += itemClub
queryClubs += ";"

# INSERT PLAYERS
clubName = data['players'][0]['club']
clubId = 1
for i in range(lenPlayers):
    player = data['players'][i]
    if(player['date-of-birth']):
        player['date-of-birth'] = str(datetime.datetime.strptime(
            player['date-of-birth'], '%b %d %Y').date())

    if (player['height']):
        player['height'] = player['height'].replace(" cm", "")
    if(player['market-value']):
        player['market-value'] = player['market-value'].replace(" euros", "")

    # clean
    item = "("
    for x in player:
        if (x == 'club' or x == 'id'):
            continue
        else:
            if(player[x]):
                item += f"\'{player[x]}\',"
            else:
                item += "NULL,"

    if(clubName != player['club']):
        clubId += 1
        clubName = player['club']
    item += f"{clubId})"
    if(i != lenPlayers-1):
        item += ','
    queryPlayers += item
queryPlayers += ";"

try:
    conn = msql.connect(host=HOST, database=DB_NAME, user=DB_USER,
                        password=DB_PASS)  # give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute(queryClubs)
        print("clubs inserted")
        cursor.execute(queryPlayers)
        print("players inserted")
        conn.commit()
        print("record inserted")
except Error as e:
    print("Error while connecting to MySQL", e)