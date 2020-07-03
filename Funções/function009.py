# Uso de parametros opcionais
# o paremetro C = 0, faz que a função rode sem receber o padrão C, sendo assim uma parametro opcional

def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de tres valores e mostra o resultado na tela.
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    Função criada pro Gustavo Guanabara do canal CursoemVideo.
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(1, 4, 5)
somar(2, 3)
help(somar)
#