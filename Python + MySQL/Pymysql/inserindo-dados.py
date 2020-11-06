import pymysql

con = pymysql.connect(db='garagem', user='root', passwd='lucas')

cursor = con.cursor()

# Inserção de qualquer pessoa pelo terminal
placa = input('Digite a placa a ser inserida: ')

if len(placa) != 8:
    print('Placa Invalida')
    exit()

dono = input('Digite o nome do dona a ser inserido: ')


cursor.execute(f"INSERT INTO carros (placa, nome_dono) VALUES ('{placa}', '{dono}')")


con.commit()

con.close()