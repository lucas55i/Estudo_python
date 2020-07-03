# Escopo de variáveis

def teste():
    # Variavel local
    x = 8
    a = 22
    print(f'Na função teste, n vale {a}')
    print(f'Na função teste, a vale {a}')
    print(f'Na função teste, x vale {x}')


# Variavél global
a = 2
print(f'No programa principal, n vale {a}')
teste()
