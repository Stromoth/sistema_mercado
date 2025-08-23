import json, os

class Produto:
    def __init__(self, nome, valor, quantidade):
        self.Nome = nome
        self.Valor = float(valor)
        self.Quantidade = quantidade
    
    def editar_quantidade(self, loja):
        print('EDITAR QUANTIDADE')
        id = int(input('Insira o ID do produto\n-> ')) - 1
        print('1 - Aumentar quantidade\n2 - Diminuir quantidade')
        escolha = int(input('-> '))
        match escolha:
            case 1:
                quantidade = int(input('Quantidade a ser aumentada\n-> '))
                loja.estoque[id]['Quantidade'] += quantidade
            case 2:
                quantidade = int(input('Quantidade a ser diminuida\n-> '))
                loja.estoque[id]['Quantidade'] -= quantidade
        with open('estoque.json', 'w', encoding='utf-8') as arquivo:
            json.dump(loja.estoque, arquivo, ensure_ascii=False, indent=2)

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

            produto = vars(produto)
            self.estoque.append(produto)

            with open ('estoque.json', 'w', encoding='utf-8') as arquivo:
                json.dump(self.estoque, arquivo, ensure_ascii=False, indent=2)
                print(f'Produto {produto["Nome"]} cadastrado com sucesso')

            input('Digite 1 para voltar\n-> ')
            os.system('cls')
    
    def remover_produto(self):
        print('REMOVER PRODUTO')
        id = int(input('Insira o ID do produto que quer remover\n-> ')) - 1

        with open ('estoque.json', 'r', encoding='utf-8') as arquivo:
            self.estoque = json.load(arquivo)

        print(f'O produto {self.estoque[id]["Nome"]} será removido')
        print('Continuar?')
        print('1 - Sim\n2 - Não')

        escolha = int(input('-> '))
        match escolha:
            case 1:
                print(f'O produto {self.estoque[id]["Nome"]} foi removido do sistema')
                del self.estoque[id]
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

        with open ('estoque.json', 'r', encoding='utf-8') as arquivo:
            self.estoque = json.load(arquivo)

        for i in self.estoque:
            print(f'ID: {self.estoque.index(i) + 1}')
            for k, v in i.items():
                if k == 'Valor':
                    print(f'{k}: R${v:.2f}')
                else:
                    print(f'{k}: {v}')

            print(f'='*31)
        input('Digite 1 para voltar\n-> ')
        os.system('cls')

class Vendedor:
    def __init__(self, nome):
        self.Nome = nome
        with open('vendedor.json', 'r', encoding='utf-8') as vendedor:
            dados_do_usuario = json.load(vendedor)
            self.Saldo = dados_do_usuario['Saldo']

        with open('vendedor.json', 'w', encoding='utf-8') as vendedor:
            json.dump(vars(self), vendedor, ensure_ascii=False, indent=2)

    def vender(self, loja):
        id = int(input('Insira o ID do produto vendido\n-> ')) - 1 
        quantidade = int(input(f'\nInsira a quantidade vendida do produto {loja.estoque[id]["Nome"]}\n-> '))

        print(f'O produto vendido foi {loja.estoque[id]["Nome"]}')
        print('Confimar venda?\n1 - Confirmar\n2 - Cancelar')

        escolha = int(input('-> '))
        match escolha:
            case 1:
                if loja.estoque[id]['Quantidade'] - quantidade < 0:
                    print('Não foi possível realizar a venda.')
                    print('Quantidade de produtos insuficiente no estoque.')
                else: 
                    print(f'O vendedor {self.Nome} vendeu {quantidade} unidade(s) do produto {loja.estoque[id]["Nome"]}.')

                    valor_recebido = ( loja.estoque[id]["Valor"] ) * quantidade
                    print(f'Recebeu R${valor_recebido:.2f}.')

                    self.Saldo += valor_recebido
                    with open('vendedor.json', 'w', encoding='utf-8') as vendedor:
                        json.dump(vars(self), vendedor, ensure_ascii=False, indent=2)

                    loja.estoque[id]['Quantidade'] -= quantidade
                    with open('estoque.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(loja.estoque, arquivo, ensure_ascii=False, indent=2)

                input('Digite 1 para continuar\n-> ')
            case 2:
                input('Digite 1 para continuar\n-> ')
        os.system('cls')
    
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
