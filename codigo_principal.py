import os, json

class Mercado:
    def __init__(self, nome):
        self.nome = nome
        self.estoque = list()

    def cadastrar_produto(self, produto):
            produto = vars(produto)
            self.estoque.append(produto)
            with open ('estoque.json', 'w', encoding='utf-8') as arquivo:
                json.dump(self.estoque, arquivo, ensure_ascii=False, indent=2)
    
    def mostrar_estoque(self):
        print(f'='*31)
        print(f'Estoque da {self.nome}')
        print(f'='*31)
        with open ('estoque.json', 'r') as arquivo:
            self.estoque = json.load(arquivo)
        for i in self.estoque:
            for k, v in i.items():
                print(f'{k}: {v}')
            print(f'='*31)


os.system('cls')
loja = Mercado('EMC Produtos')

class Produto:
    def __init__(self, nome, valor, quantidade):
        self.Nome = nome
        self.Valor = f'R${float(valor):.2f}'
        self.Quantidade = quantidade

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