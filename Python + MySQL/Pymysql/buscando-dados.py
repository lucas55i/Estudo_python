import pymysql

con = pymysql.connect(db='garagem', user='root', passwd='lucas')

cursor = con.cursor()

cursor.execute("SELECT nome_dono FROM carros WHERE placa = 'kla-2135' ")

resultado = cursor.fetchall()


print('O dono do carro com a placa informada é: ')

for linha in resultado:
    print(linha)