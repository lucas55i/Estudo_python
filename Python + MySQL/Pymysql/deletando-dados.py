import pymysql

con = pymysql.connect(db='garagem', user='root', passwd='lucas')

cursor = con.cursor()
print('PARA DELETAR UM USÚARIO BASTA DIGITAR A PLCA DA VEICULO')
deletar = input('Qual a placa a ser deletada: ')

cursor.execute(f"DELETE FROM carros WHERE Placa = '{deletar}' ")
con.commit()

con.close()