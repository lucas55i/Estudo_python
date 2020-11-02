import mysql.connector

con = mysql.connector.connect(
    host='localhost',
    database='db_MeusLivrios',
    user='root',
    password='lucas'
)

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor", db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao Banco de dados", linha)


if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão encerrada")