from .produto import Produto
from json import load, dump
from .funcoes import gerar_id, encontrar_produto
from os import system, path

class Mercado(Produto):
    def __init__(self, nome):
        self.nome = nome
        try:
            with open ('estoque.json', 'r', encoding='utf-8') as arquivo:
                self.estoque = load(arquivo)
        except:
            self.estoque = list()
            
    def cadastrar_produto(self):
            print('CADASTRAR PRODUTO')

            nome = input('Nome: ')
            preco = float(input('Preço: '))
            quantidade = int(input('Quantidade: '))

            produto = Produto(nome, preco, quantidade)
            
            dict_produto = {
                'ID':gerar_id(),
                'Nome':produto.Nome,
                'Preço':produto.Valor,
                'Quantidade':produto.Quantidade
            }

            self.estoque.append(dict_produto)

            with open ('estoque.json', 'w', encoding='utf-8') as arquivo:
                dump(self.estoque, arquivo, ensure_ascii=False, indent=2)
                print(f'Produto {dict_produto["Nome"]} cadastrado com sucesso')

            input('Digite 1 para voltar\n-> ')
            system('cls')
    
    def remover_produto(self):
        print('REMOVER PRODUTO')

        id = int(input('Insira o ID do produto que quer remover\n-> '))
        produto_encontrado = encontrar_produto(self.estoque, id)

        with open ('estoque.json', 'r', encoding='utf-8') as arquivo:
            self.estoque = load(arquivo)
        system('cls')

        print(f'O produto {produto_encontrado["Nome"]} será removido')
        print('Continuar?')
        print('1 - Sim\n2 - Não')

        escolha = int(input('-> '))
        system('cls')

        match escolha:
            case 1:
                print(f'O produto {produto_encontrado["Nome"]} foi removido do sistema')
                self.estoque.remove(produto_encontrado)
                with open ('estoque.json', 'w', encoding='utf-8') as arquivo:
                    dump(self.estoque, arquivo, ensure_ascii=False, indent=2)
                input('Digite 1 para continuar\n-> ')
                system('cls')

            case 2:
                print('Ação cancelada')
                input('Digite 1 para continuar\n-> ')
                system('cls')
    
    def mostrar_estoque(self):
        print(f'='*31)
        print(f'Estoque da {self.nome}')
        print(f'='*31)
        if path.exists('estoque.json'):
            with open ('estoque.json', 'r', encoding='utf-8') as arquivo:
                self.estoque = load(arquivo)
        else:
            with open ('estoque.json', 'a', encoding='utf-8') as arquivo:
                dump(' ', arquivo)

        for i in self.estoque:
            for k, v in i.items():
                if k == 'Preço':
                    print(f'{k}: R${v:.2f}')
                else:
                    print(f'{k}: {v}')

            print(f'='*31)
        input('Digite 1 para voltar\n-> ')
        system('cls')
    
    def reordenar_estoque(self):
        print(f'='*31)
        print(f'Reordenar estoque')
        print(f'='*31)

        print('1 - Ordenar por nome(A-Z)')
        print('2 - Ordenar por preço(Menor-Maior)')
        print('3 - Ordenar por quantidade em estoque(Mais-Menos)')
        print('4 - Ordenar por ID(Menor-Maior)')

        escolha = int(input('-> '))
        system('cls')

        match escolha:
            case 1:
                self.estoque = sorted(self.estoque, key=lambda x: x['Nome'])
                print('Estoque ordenado em ordem alfabética.')
            case 2:
                self.estoque = sorted(self.estoque, key=lambda x: x['Preço'])
                print('Estoque ordenado com base nos preços.')
            case 3:
                self.estoque = sorted(self.estoque, key=lambda x: x['Quantidade'], reverse=True)
                print('Estoque ordenado com base nas quantidades.')
            case 4: 
                self.estoque = sorted(self.estoque, key=lambda x: x['ID'])
                print('Estoque ordenado com base nos IDs.')
        with open('estoque.json', 'w', encoding='utf-8') as arquivo:
            dump(self.estoque, arquivo, ensure_ascii=False, indent=2)
        print(f'='*31)

        input('Digite 1 para continuar\n-> ')
        system('cls')
