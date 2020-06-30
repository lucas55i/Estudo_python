#Estudo sobre dicionários

#semelhantes as listas e as tuplas, podendo ter indices literais


dados = dict()
dados = {'nome': 'Lucas', 'idade': 25}


#Para inserir dados no dicionário.
dados['sexo'] = 'M'

print(dados['nome'])
print(dados['idade'])
print(dados['sexo'])

#Outro exemplo.

filmes = {'titulo': 'Star Wars',
          'ano': 1977,
          'diretor': 'George Lucas'
          }

print(filmes.values()) #.Values retorna todos os valores do dicionário
print(filmes.keys()) #.Keys retorna todas as chaves do dicionário
print(filmes.items()) #.Items retorna todos os valores do dicionário