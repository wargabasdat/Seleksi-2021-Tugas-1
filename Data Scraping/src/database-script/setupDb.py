import mysql.connector as msql
from mysql.connector import Error
from decouple import config

# load .env variables
HOST = config('HOST')
DB_USER = config('DB_USER')
DB_PASS = config('DB_PASS')
DB_NAME = config('DB_NAME')

# CREATE TABLE Clubs
createClub = '''CREATE TABLE IF NOT EXISTS Clubs (
    clubId INT(11) AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    manager VARCHAR(100),
    league VARCHAR(50),
    stadium VARCHAR(100)
);
'''
createPlayer = '''CREATE TABLE IF NOT EXISTS Players (
    playerId INT(11) AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    number VARCHAR(4),
    position VARCHAR(100),
    birthDate DATE,
    nationality VARCHAR(100),
    height INT(11),
    foot ENUM('left', 'right', 'both'),
    marketValue INT(11),
    clubId INT(11),
    FOREIGN KEY (clubId) REFERENCES Clubs(clubId)
);
'''

try:
    mydb = msql.connect(
        host=HOST, user=DB_USER,
        password=DB_PASS)

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS " + DB_NAME)
except Error as e:
    print("Error while connecting to MySQL", e)

try:
    conn = msql.connect(host=HOST, user=DB_USER,
                        password=DB_PASS, database=DB_NAME)  # give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute(createClub)
        cursor.execute(createPlayer)
        print("Tabel berhasil dimasukan")
        conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)