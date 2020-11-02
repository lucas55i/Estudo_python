import pymysql

con = pymysql.connect(db='garagem', user='root', passwd='lucas')

curso = con.cursor()

curso.execute("UPDATE carros SET nome_dono = 'pedro' WHERE placa = 'acC-1234'")

con.commit()

con.close