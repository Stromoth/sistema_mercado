from .funcoes import encontrar_produto
from os import system
from json import dump

class Produto:
    def __init__(self, nome, valor, quantidade):
        self.Nome = nome
        self.Valor = float(valor)
        self.Quantidade = quantidade
    
    def editar_quantidade(self, loja):
        print('EDITAR QUANTIDADE')
        id = int(input('Insira o ID do produto\n-> '))
        produto_encontrado = encontrar_produto(loja.estoque, id)
        system('cls')

        print(f'Editando quantidade do produto {produto_encontrado["Nome"]}')
        print('1 - Aumentar quantidade\n2 - Diminuir quantidade')
        escolha = int(input('-> '))
        system('cls')

        match escolha:
            case 1:
                print(f'Editando quantidade do produto {produto_encontrado["Nome"]}')
                quantidade = int(input('Quantidade a ser aumentada\n-> '))
                produto_encontrado['Quantidade'] += quantidade
            case 2:
                print(f'Editando quantidade do produto {produto_encontrado["Nome"]}')
                quantidade = int(input('Quantidade a ser diminuida\n-> '))
                produto_encontrado['Quantidade'] -= quantidade
        with open('estoque.json', 'w', encoding='utf-8') as arquivo:
            dump(loja.estoque, arquivo, ensure_ascii=False, indent=2)
        
        input('Digite 1 para continuar\n-> ')
        system('cls')
