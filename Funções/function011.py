# Retorno de valores, muito útil quando se deseja personalização dos resultados

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(3, 2, 3)
r2 = soma(2, 3, 5)
r3 = soma(6, 4, 3)

print(f'Meus cáluclos deram {r1}, {r2} e {r3}.')
 