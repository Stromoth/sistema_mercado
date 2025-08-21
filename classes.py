import json

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

class Produto:
    def __init__(self, nome, valor, quantidade):
        self.Nome = nome
        self.Valor = f'R${float(valor):.2f}'
        self.Quantidade = quantidade