import os
from classes import Mercado, Vendedor

os.system('cls')
loja = Mercado('EMC Produtos')
vendedor = Vendedor('Gabriel')

while True:
    print(f'Sistema da {loja.nome}')
    print('1 - Gerenciar estoque')
    print('2 - Vender')
    print('3 - Ver saldo')
    print('4 - Sair')
    escolha = int(input('-> '))

    os.system('cls')
    match escolha:
        case 1: # Gerenciar estoque
            while True:
                print(f'Sistema da {loja.nome}')
                print('1 - Cadastrar produto')
                print('2 - Remover produto')
                print('3 - Editar produto')
                print('4 - Ver estoque')
                print('5 - Voltar')

                escolha = int(input('-> '))
                os.system('cls')
                match escolha:
                    case 1:
                        loja.cadastrar_produto()
                    case 2:
                        loja.remover_produto()
                    case 3:
                        loja.editar_quantidade(loja)
                    case 4:
                        loja.mostrar_estoque()
                    case 5:
                        os.system('cls')
                        break
        case 2: # Vender
            vendedor.vender(loja)
        case 3: # Ver saldo
            vendedor.ver_saldo()
        case 4: # Sair
            break
