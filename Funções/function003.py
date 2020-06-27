def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B é = {s}')

#Simplifcando chamando a função soma
#Caso não esteja especificando os paremetros dentro da função soma o programa mesmo considera os valores.


soma(8, 9)

#a = 4
#b = 5
#s = a + b
#print(s)
print('-' * 30)


def multiplicao(a, b):
    print(f'A = {a} e B = {b}')
    s = a * b
    print(f'A Multiplicação de A * B é = {s}')


multiplicao(2, 5)

print('-' * 30)

def subtracao(a, b):
    print(f'A = {a} e B = {b}')
    s = a - b
    print(f'A Subtração de A - B é = {s}')


subtracao(8, 5)

print('-' * 30)

def divisão(a, b):
    print(f'A = {a} e B = {b}')
    s = a / b
    print(f'A divisão entre A / B é = {s}')


divisão(10, 2)