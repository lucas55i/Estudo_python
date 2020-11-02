import pymysql

con = pymysql.connect(db='garagem', user='root', passwd='lucas')

cursor = con.cursor()

cursor.execute("DELETE FROM carros WHERE Placa = 'ABC-1234' ")
con.commit()

con.close()