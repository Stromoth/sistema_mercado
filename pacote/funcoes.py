from json import load, dump
from os import path
from itertools import count
from functools import wraps
from datetime import datetime

def log_vendas(func):
    @wraps(func)
    def wrapper(self, loja, *args, **kwargs):
        resultado = func(self, loja, *args, **kwargs)
        if isinstance(resultado, tuple) and len(resultado) == 2:
            nome, quantidade = resultado
            with open('log_vendas.txt', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Produto: {nome} - Quantidade: {quantidade}\n")
        return resultado
    return wrapper

def gerar_id():
    if path.exists("id.json"):
        with open("id.json", "r") as arquivo:
            ultimo_id = load(arquivo)
    else:
        ultimo_id = 0 

    contador = count(ultimo_id + 1)

    novo_id = next(contador)

    with open("id.json", "w") as arquivo:
        dump(novo_id, arquivo)

    return novo_id

def encontrar_produto(estoque, id_procurado):
    for produto in estoque:
        if produto["ID"] == id_procurado:
            return produto
    return None
