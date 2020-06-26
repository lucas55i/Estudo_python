#como abrir arquivos csv

import pandas as pd

df = pd.read_csv('dados/Dados aula 1.csv', encoding="UTF-8", sep=";")

df = pd.read_csv('dados/Dados aula 1.csv', encoding="UTF-8", sep=";", header=0)#Especifia para fazer a listagem a partir de 0

df = pd.read_csv('dados/Dados aula 1.csv', encoding="UTF-8", sep=";", usecols=['AddressID', 'AddressLine2', 'City', 'StateProvinceID', 'PostalCode'])#Usecols devolve a ou as colunas que voce deseja ver (os nomes devem estar identicos

df = pd.read_csv('dados/Dados aula 1.csv', encoding="UTF-8", sep=";", usecols=['AddressID', 'AddressLine2'], nrows=200)#NROWS serve para ler somente até os número de linhas desejado


print(df)