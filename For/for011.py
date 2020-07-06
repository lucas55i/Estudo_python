somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print(f'-----{p}° PESSOA -----')
    nome = str(input('Nome: ')).strip()  # strip() Tira os espaços
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()  # strip() tira os espaços
    somaidade += idade

    #Vertifica se a primeira pessoa é homem
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome

    #Verifica se a primeira pessoa é homeme checa a idade
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    #Verifica quantas mulheres tem menops de 20 anos
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4

print(f'A média de idade do grupo é de {médiaidade} anos. ')
print(f'O homen mais velho tem {maioridadehomem} anos e se chama {nomevelho}. ')
print(f'Ao todo são {totmulher20} com menor de 20 anos. ')
