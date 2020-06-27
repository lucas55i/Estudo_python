#Empacotamento,

#Como o print devolve uma tupla da pra fazer de varias formas (TUPLAS NÃO PODEM SER ALTERADAS)


def contador(*núm):
    contar = len(núm)
    print(f'Recibo os valores {núm} e são ao todo {contar} número')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

