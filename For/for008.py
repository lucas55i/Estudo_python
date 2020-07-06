# Palindromo

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.strip()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O iverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase não pe um palíndromo')
