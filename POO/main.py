from pessoa import Pessoa

p1 = Pessoa('Lucas', 21)
p1.comer('maçã')
p1.para_comer()
print('-' * 30)

p1.falar('POO')
p1.para_falar()
print('-' * 30)

p1.comer('Banana')
p1.falar('POO')
print('-' * 30)

p1.para_comer()
p1.falar('Vida')
print('-' * 30)

print('FIM')