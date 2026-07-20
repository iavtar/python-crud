import mysql.connector

def getConnection():
    return mysql.connector.connect(
        host="localhost",
        user = "root",
        password = "toor",
        database = "proj101"
    )

