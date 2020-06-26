# Estudo sobre funções

produtos = []


def cadastrarProduto(produto):
    global produtos
    produtos.append(produto)


def listaProdutos():
    global produtos
    for p in produtos:
        print(p)


produto = ""
while produto != ("sair"):
    produto = input('Digite o produto que deseja cadastar: ')
    cadastrarProduto(str(produto))
    print("produtos cadastrados")
    listaProdutos()
