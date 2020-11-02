import mysql.connector

# Conexão
con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='lucas'
)

cursor = con.cursor()
cursor.execute("create database Lucas")
cursor.close()
