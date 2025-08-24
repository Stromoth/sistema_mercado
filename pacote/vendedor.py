from .funcoes import log_vendas, encontrar_produto
from os import system
from json import dump, load

class Vendedor:
    def __init__(self, nome):
        self.Nome = nome
        try:
            with open('vendedor.json', 'r', encoding='utf-8') as vendedor:
                dados_do_usuario = load(vendedor)
                self.Saldo = dados_do_usuario['Saldo']
        except:
            self.Saldo = 0

        with open('vendedor.json', 'w', encoding='utf-8') as vendedor:
            dump(vars(self), vendedor, ensure_ascii=False, indent=2)

    @log_vendas
    def vender(self, loja):
        id = int(input('Insira o ID do produto vendido\n-> '))
        produto_encontrado = encontrar_produto(loja.estoque, id)
        system('cls')

        quantidade = int(input(f'Insira a quantidade vendida do produto {produto_encontrado["Nome"]}\n-> '))
        system('cls')

        print(f'CONFIRMAR VENDA\nProduto: {produto_encontrado["Nome"]}\nQuantidade: {quantidade}')
        print('\n1 - Confirmar\n2 - Cancelar')
        escolha = int(input('-> '))
        system('cls')

        match escolha:
            case 1:
                if produto_encontrado['Quantidade'] - quantidade < 0:
                    print('Não foi possível realizar a venda.')
                    print('Quantidade de produtos insuficiente no estoque.')
                else: 
                    print(f'O vendedor {self.Nome} vendeu {quantidade} unidade(s) do produto {produto_encontrado["Nome"]}.')

                    valor_recebido = ( produto_encontrado["Preço"] ) * quantidade
                    print(f'Recebeu R${valor_recebido:.2f}.')

                    self.Saldo += valor_recebido
                    with open('vendedor.json', 'w', encoding='utf-8') as vendedor:
                        dump(vars(self), vendedor, ensure_ascii=False, indent=2)

                    produto_encontrado['Quantidade'] -= quantidade
                    with open('estoque.json', 'w', encoding='utf-8') as arquivo:
                        dump(loja.estoque, arquivo, ensure_ascii=False, indent=2)
                    return (produto_encontrado['Nome'], quantidade)

                input('Digite 1 para continuar\n-> ')
            case 2:
                input('Digite 1 para continuar\n-> ')
        system('cls')
    
    def ver_saldo(self):
        with open('vendedor.json', 'r', encoding='utf-8') as vendedor:
            dados_do_usuario = load(vendedor)

        print('SEU SALDO')
        for k, v in dados_do_usuario.items():
            if k == 'Saldo':
                print(f'{k}: R${v:.2f}')
            else:
                print(f'{k}: {v}')
        input('Digite 1 para continuar\n-> ')
        system('cls')
