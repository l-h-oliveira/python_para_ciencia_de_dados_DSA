# %%

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from time import time

from IPython import display


# %%
# Exercício 2
# Crie um array NumPy com 1000000 e uma lista com 1000000. Multiplique cada elemento do array e da lista por 2 e calcule o tempo de execução com cada um dos objetos (use %time). Qual objeto oferece melhor performance, array NumPy ou lista?

# Medindo o tempo usando o NumPy
t1 = time()

np1 = np.arange(1000000)
np2 = 2*np1

t_np = time() - t1
print('O tempo de execução da tarefa com numpy  é {}.'.format( t_np))

# Medindo o tempo com listas

t2 = time()

# l1 = [i for i in range(1000000)]
l2 = list(map(lambda x: 2*x, range(1000000)))

t_l = time() - t2
print('\nO tempo de execução da tarefa com litas  é {}.'.format( t_l))

print('\nO Numpy é {} mais rápido.'.format(t_l/t_np))

# %%
# Exercício 2
# Crie um array de 10 elementos
# Altere o valores de todos os elementos dos índices 5 a 8 para 0

np2 = np.random.randn(10)
np2[5:9] = 0
print(np2)

# %%
# Exercício 3
# Crie um array de 3 dimensões e imprima a dimensão 1 

np3 = np.array([[[1,2], [3,4]], [[5, 6], [7,8]]])
print(np3.shape)
print(np3[0, :, :])
# %%
# Exercício 4
# Crie um array de duas dimensões (matriz).
# Imprima os elementos da terceira linha da matriz
# Imprima todos os elementos da primeira e segunda linhas e segunda e terceira colunas

np4 = 10*np.random.rand(4, 4)

print(np4[2, :])
print(np4[0, :])
print(np4[1, :])
print(np4[:, 1])
print(np4[:, 2])

# %%
# Exercício 5
# Calcule a transposta da matriz abaixo
arr = np.arange(15).reshape((3, 5))

# Usamos o método implementado pelo Numpy
print(arr.transpose())

# %%
# Exercício 6
# Considere os 3 arrays abaixo
# Retorne o valor do array xarr se o valor for True no array cond. Caso contrário, retorne o valor do array yarr.
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

for i in range(len(xarr)):
    if cond[i]:
        print(xarr[i])
    else:
        print(yarr[i])        

# %%
# Exercício 7
# Crie um array A com 10 elementos e salve o array em disco com a extensão npy Depois carregue o array do disco no array B

A = np.arange(10)
print('Array A: ', A)

np.savetxt('A.npy', A)

B = np.loadtxt('A.npy', dtype = int)
print('Array B: ', B)

# %%
# Exercício 8
# Considerando a série abaixo, imprima os valores únicos na série
obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'a', 'b'])

print('\nobj')
print(obj)

# vamos usar o método do pandas unique
print('\nelementos únicos')
print(obj.unique())

# %%
# Exercício 9
# Considerando o trecho de código que conecta em uma url na internet, imprima o dataframe conforme abaixo.
import requests
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)

# Examinando o conteúdo da resposta
print(resp.text)

#Já que o resultado é parecido com um dicionário do Python, podemos utilizar um método que converte a resposta para um objeto json

resp_json = resp.json()

# Agora, podemos utilizar a função do pandas para construir o DataFrame
df = pd.DataFrame(resp_json, columns = ['number', 'title', 'labels', 'state'])

display(df)
# %%
# Exercício 10
# Crie um banco de dados no SQLite, crie uma tabela, insira registros,  consulte a tabela e retorne os dados em dataframe do Pandas
import sqlite3 as sql

# Iniciando a conexão com o banco de dados. caso o banco de dados não exista, ele será criado
my_conn = sql.connect('exerc_10.db')

# Criando a tabela impostos. A coluna ESTADO é do tipo caractere e a coluna ICMS é do tipo float
query1 = 'CREATE TABLE impostos (ESTADO VARCHAR(20), ICMS FLOAT(11))'

my_conn.execute(query1)

# %%
# Inserindo dados na tabela
query2 = 'INSERT INTO impostos (ESTADO, ICMS) VALUES ("Minas Gerais", 30), ("Rio de Janeiro", 32), ("São Paulo",  25), ("Rio Grande do Sul", 23);'

my_conn.execute(query2)

# Comitanto (tornando as modificações permanentes no bando de dados)
my_conn.commit()

# %%
# Exibindo os dados inseridos através de um dataframe
query3 = 'SELECT * FROM impostos LIMIT 5'
pd.read_sql_query(query3, my_conn)

# Fechando a conexão com o banco de dados
my_conn.close()
# %%
