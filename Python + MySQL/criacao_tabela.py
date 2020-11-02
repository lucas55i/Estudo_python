#Criação da tabela dentro do banco que foi criado no arquivo crud.py
import mysql.connector

con = mysql.connector.connect(
    host='localhost',
    database="Lucas",
    user='root',
    password='lucas'
)

cursor = con.cursor()
cursor.execute("create table student(roll INT, name VARCHAR(255)")
cursor.close()
