# peso de 5 pessoas

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f'Peso da {p}º pessa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lindo for de {maior} Kg')
print(f'O menor peso lido foi de {menor} Kg')