import json, os
from itertools import count
from functools import wraps

'''def log_vendas(func):
    @wraps(func)
    def wrapper(produto, quantidade):

        return wrapper'''

def gerar_id():
    if os.path.exists("id.json"):
        with open("id.json", "r") as arquivo:
            ultimo_id = json.load(arquivo)
    else:
        ultimo_id = 0 

    contador = count(ultimo_id + 1)

    novo_id = next(contador)

    with open("id.json", "w") as arquivo:
        json.dump(novo_id, arquivo)

    return novo_id

def encontrar_produto(estoque, id_procurado):
    for produto in estoque:
        if produto["ID"] == id_procurado:
            return produto
    return None

class Produto:
    def __init__(self, nome, valor, quantidade):
        self.Nome = nome
        self.Valor = float(valor)
        self.Quantidade = quantidade
    
    def editar_quantidade(self, loja):
        print('EDITAR QUANTIDADE')
        id = int(input('Insira o ID do produto\n-> '))
        produto_encontrado = encontrar_produto(loja.estoque, id)
        os.system('cls')

        print(f'Editando quantidade do produto {produto_encontrado["Nome"]}')
        print('1 - Aumentar quantidade\n2 - Diminuir quantidade')
        escolha = int(input('-> '))
        os.system('cls')

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
            json.dump(loja.estoque, arquivo, ensure_ascii=False, indent=2)
        
        input('Digite 1 para continuar\n-> ')
        os.system('cls')

class Mercado(Produto):
    def __init__(self, nome):
        self.nome = nome
        try:
            with open ('estoque.json', 'r', encoding='utf-8') as arquivo:
                self.estoque = json.load(arquivo)
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
                json.dump(self.estoque, arquivo, ensure_ascii=False, indent=2)
                print(f'Produto {dict_produto["Nome"]} cadastrado com sucesso')

            input('Digite 1 para voltar\n-> ')
            os.system('cls')
    
    def remover_produto(self):
        print('REMOVER PRODUTO')

        id = int(input('Insira o ID do produto que quer remover\n-> '))
        produto_encontrado = encontrar_produto(self.estoque, id)

        with open ('estoque.json', 'r', encoding='utf-8') as arquivo:
            self.estoque = json.load(arquivo)
        os.system('cls')

        print(f'O produto {produto_encontrado["Nome"]} será removido')
        print('Continuar?')
        print('1 - Sim\n2 - Não')

        escolha = int(input('-> '))
        os.system('cls')

        match escolha:
            case 1:
                print(f'O produto {produto_encontrado["Nome"]} foi removido do sistema')
                self.estoque.remove(produto_encontrado)
                with open ('estoque.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(self.estoque, arquivo, ensure_ascii=False, indent=2)
                input('Digite 1 para continuar\n-> ')
                os.system('cls')

            case 2:
                print('Ação cancelada')
                input('Digite 1 para continuar\n-> ')
                os.system('cls')
    
    def mostrar_estoque(self):
        print(f'='*31)
        print(f'Estoque da {self.nome}')
        print(f'='*31)
        if os.path.exists('estoque.json'):
            with open ('estoque.json', 'r', encoding='utf-8') as arquivo:
                self.estoque = json.load(arquivo)
        else:
            with open ('estoque.json', 'a', encoding='utf-8') as arquivo:
                json.dump(' ', arquivo)

        for i in self.estoque:
            for k, v in i.items():
                if k == 'Preço':
                    print(f'{k}: R${v:.2f}')
                else:
                    print(f'{k}: {v}')

            print(f'='*31)
        input('Digite 1 para voltar\n-> ')
        os.system('cls')
    
    def reordenar_estoque(self):
        print(f'='*31)
        print(f'Reordenar estoque')
        print(f'='*31)

        print('1 - Ordenar por nome(A-Z)')
        print('2 - Ordenar por preço(Menor-Maior)')
        print('3 - Ordenar por quantidade em estoque(Mais-Menos)')
        print('4 - Ordenar por ID(Menor-Maior)')

        escolha = int(input('-> '))
        os.system('cls')

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
            json.dump(self.estoque, arquivo, ensure_ascii=False, indent=2)
        print(f'='*31)

        input('Digite 1 para continuar\n-> ')
        os.system('cls')
        
class Vendedor:
    def __init__(self, nome):
        self.Nome = nome
        try:
            with open('vendedor.json', 'r', encoding='utf-8') as vendedor:
                dados_do_usuario = json.load(vendedor)
                self.Saldo = dados_do_usuario['Saldo']
        except:
            self.Saldo = 0

        with open('vendedor.json', 'w', encoding='utf-8') as vendedor:
            json.dump(vars(self), vendedor, ensure_ascii=False, indent=2)

    '''@log_vendas'''
    def vender(self, loja):
        id = int(input('Insira o ID do produto vendido\n-> '))
        produto_encontrado = encontrar_produto(loja.estoque, id)
        os.system('cls')

        quantidade = int(input(f'Insira a quantidade vendida do produto {produto_encontrado["Nome"]}\n-> '))
        os.system('cls')

        print(f'CONFIRMAR VENDA\nProduto: {produto_encontrado["Nome"]}\nQuantidade: {quantidade}')
        print('\n1 - Confirmar\n2 - Cancelar')
        escolha = int(input('-> '))
        os.system('cls')

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
                        json.dump(vars(self), vendedor, ensure_ascii=False, indent=2)

                    produto_encontrado['Quantidade'] -= quantidade
                    with open('estoque.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(loja.estoque, arquivo, ensure_ascii=False, indent=2)

                input('Digite 1 para continuar\n-> ')
            case 2:
                input('Digite 1 para continuar\n-> ')
        os.system('cls')
        '''return produto_encontrado['Nome'], quantidade'''
    
    def ver_saldo(self):
        with open('vendedor.json', 'r', encoding='utf-8') as vendedor:
            dados_do_usuario = json.load(vendedor)

        print('SEU SALDO')
        for k, v in dados_do_usuario.items():
            if k == 'Saldo':
                print(f'{k}: R${v:.2f}')
            else:
                print(f'{k}: {v}')
        input('Digite 1 para continuar\n-> ')
        os.system('cls')
