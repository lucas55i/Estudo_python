# Usando docstrings, podemos colocar o manual completo de funções criadas pelo programador

def contador(i, f, p):
    """
    ->Faz uma contagem e a mostra na tela
    :param i: Início da contage
    :param i: FIm da Contagem
    :param p: Passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!!')


contador(2, 10, 2)

help(contador)
#