# Exercício de  com uso de listas e dicionários

nome = {}
nota = []

for c in range(0, 1):
    nome['Aluno'] = str(input('Nome: '))
    nome['Nota'] = float(input('Nota: '))
    nota.append(nome.copy())

for n in nota:
    for k, v in n.items():
        if nome['Nota'] > 7:
            print(f'Nome é igual a ', nome['Aluno'])
            print(f'A Média é igual a ', nome['Nota'])
            print('Situação é igual a Reprovado')

        else:
            print(f'Nome é igual a ', nome['Aluno'])
            print(f'A Média é igual a ', nome['Nota'])
            print('Situação é igual a Reprovado')

        exit()
