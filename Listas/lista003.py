#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
#lista = [0, 1, 2, 3, 4]

#for inteiros in lista:
#    print(inteiros)

#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
#lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#lista.sort(reverse=True)
#print(lista)

#Juntadno listas
#list_a = [1, 2, 3, 4]
#list_b = list_a
#print(list_b)

#a = [5, 6, 7, 8]
#b = [9, 10, 11, 12]
#c = a + b
#print(c)

#c += [13, 14, 15, 16]
#print(c)

#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

#def conta_consoantes(string):
   # string = string.lower() # para que a comparação não seja sensível a maiuscula/minuscula
#    consoantes = 'recíproco'
 #   return {i: string.count(i) for i in consoantes if i in string}

#print(conta_consoantes('bcdfghjklmnpqrstvwxyz'))



#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

num = []
valor = 0
par = []
impar = []

for c in range(1, 20):
    if valor % 2 == 0:
        par[0].append(valor)
    else:
        impar[1].append(valor)

print(num)