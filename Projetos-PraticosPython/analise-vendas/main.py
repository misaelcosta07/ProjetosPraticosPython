# Importação da biblioteca para manipulação de dados em tabelas
import pandas as pd  
# Importação da biblioteca NumPy para operações matemáticas e arrays
import numpy as np  
# Importação da biblioteca Matplotlib para geração de gráficos
import matplotlib.pyplot as plt  
# Importação da biblioteca Seaborn para visualização estatística de dados
import seaborn as sns  
# Importação da biblioteca random para geração de números aleatórios
import random  
# Importação das classes datetime e timedelta para manipulação de datas e intervalos de tempo
from datetime import datetime, timedelta  
#plt.show() substitui o %matplotib inline do jupyter 

# definir a funçao para gerar dados ficticios 
def 
:
    #gerar dados ficticios com panda = dataframe
    #inicar a quantidade de re
    # gistros a serem gerados 
    print(f"\nIniciando a geração de {registros} registros de vendas...")

    # criar o dicionario com categorias e preços 
    produtos = {
        'Laptop gamer': {'categoria': 'Eletronicos', 'preco': 7500.00},
        'Teclado mecanico': {'categoria': 'Acessorios', 'preco': 250.00},
        'Mouse ergonomico': {'categoria': 'Acessorios', 'preco': 170.00},
        'Monitor ultrawide': {'categoria': 'Eletronicos', 'preco': 3500.00},
        'Cadeira gamer': {'categoria': 'Moveis', 'preco': 450.00},
        'Fone headset 7.1 ': {'categoria': 'Acessarios', 'preco': 230.00},
        'SSD 1TB': {'categoria': 'hardware', 'preco': 4000.00},
        'webcam': {'categoria': 'Eletronicos', 'preco': 430.00}
    }
    #criar um lista so com os nomes do produtos
    lista_produtos = list(produtos.keys())

    #dicionario com os estados e respectivas cidades
    cidades_estados = {
        'Sao paulo': 'SP', 'Rio de janeiro': 'RJ', 'Salvador': 'BA',
        'Belo Horizonte': 'BH','Curitiba': 'PR', 'Porto Alegre': 'RS', 'Fortaleza': 'CE'
    }
    #lista so com o nome das cidades
    lista_cidades = list(cidades_estados.keys())

    #lista vai armazenar os registros de vendas 
    dados_vendas = []

    #data inical dos pedidos 
    data_inicial = datetime(2026, 1, 1)

    #criar um loop para gerar os registros de vendas 
    for i in range(registros):
        #seleciona um produto aleatoriamente
        produto_nome = random.choice(lista_produtos)
        #seleciona uma cidade aleatoriamente
        cidade = random.choice(lista_cidades)

        #calcula uma quantidade de pedidos de 1a7
        quantidade = np.random.randint(1,8)

        #calcula a data do pedido na data inicial 
        data_pedido = data_inicial + timedelta(days = int(i/5), hours = random.randint(0,23))

        # mouse ou teclado irao ter 10% de desconto
        if produto_nome in ['Mouse ergonomico', 'Teclado mecanico']:
            preco_unitario = produtos[produto_nome]['preco'] * np.random.uniform(0.9, 1.0)
        else : 
            preco_unitario = produtos[produto_nome]['preco']

        #adicioma um registro de venda a lista 
        dados_vendas.append({
            'ID pedido': 1000 + i, 
            'data_pedido': data_pedido, 
            'Nome_produto': produto_nome, 
            'Categoria': produtos[produto_nome]['categoria'], 
            'Preco_unitario': round(preco_unitario, 2), 
            'Quantidade': quantidade, 
            'ID_client': np.random.randint(100,150), 
            'Cidade': cidade, 
            'Estaado': cidades_estados[cidade] 
        })

    # mensagem de geraçao de dados
    print("Geração de dados concluida.\n")

    #retorna os dados formatados no dataframe 
    return pd.DataFrame(dados_vendas)