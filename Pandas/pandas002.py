# como abrir aquivos exel

import pandas as pd

# Abrindo arquivo, tavel peça que instale xlrd uma extenção para exel.
df = pd.read_excel("dados/Dados aula 2.xlsx")

# Especificar qual aba abrir com o uso do sheet_name
df = pd.read_excel("dados/Dados aula 2.xlsx", sheet_name=0)

arquivo_exel = pd.ExcelFile('dados/Dados aula 2.xlsx')

arquivo_exel.sheet_names
['0', '1']

aba1 = (arquivo_exel).parse(0)
aba2 = (arquivo_exel).parse(1)

print(aba2)
