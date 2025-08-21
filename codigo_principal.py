import os
from classes import Mercado, Produto

os.system('cls')
loja = Mercado('EMC Produtos')

while True:
    print(f'Sistema da {loja.nome}')
    print('1 - Cadastrar Produto')
    print('2 - Ver Estoque')
    print('3 - Sair')
    escolha = int(input('-> '))
    os.system('cls')
    match escolha:
        case 1:
            print('CADASTRAR PRODUTO')
            nome = input('Nome: ')
            preco = input('Preço: ')
            quantidade = int(input('Quantidade: '))
            produto = Produto(nome, preco, quantidade)
            loja.cadastrar_produto(produto)
            os.system('cls')
        case 2:
            loja.mostrar_estoque()
            input('Digite 1 para voltar\n-> ')
            os.system('cls')
        case 3:
            break
