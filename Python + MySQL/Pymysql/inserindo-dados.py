import pymysql

con = pymysql.connect(db='garagem', user='root', passwd='lucas')

cursor = con.cursor()

cursor.execute("INSERT INTO carros (placa, nome_dono) VALUES ('kla-2135', 'Lukinha rei delas')")

con.commit()

con.close()