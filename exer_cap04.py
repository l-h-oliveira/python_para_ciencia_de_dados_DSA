# %%
# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.
L1 = [i**3 for i in range(3)]

print(L1)

# %%
# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print (i)

L2 = list(map(lambda w: [w.upper(), w.lower(), len(w)], palavras))

for i in L2:
    print (i)

# %%
# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
matrix = [[1, 2],[3,4],[5,6],[7,8]]

L3 = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

print(matrix, L3)
# %%
# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 1, 2, 3, 4]

L4 = list(map(lambda x: [x**2, x**3], lista))

print(L4)

# %%
# Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado 
# ao elemento correspondente na listaB.
listaA = [2, 3, 4]
listaB = [10, 11, 12]

L5 = [listaA[i]**listaB[i] for i in range(len(listaA))]

print(L5)

# %%
# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar apenas os valores negativos.
print(list(filter(lambda x: x < 0, range(-5, 5))))

# %%
# Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]

print( list( filter( lambda x: x in b, a)))

# %%
# Exercício 8 - Considere o código abaixo. Obtenha o mesmo resultado usando o pacote time. 
# Não conhece o pacote time? Pesquise!
import datetime
print (datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))

import time as tm

print(tm.strftime("%d/%m/%Y %H:%M"))

# %%
# Exercício 9 - Considere os dois dicionários abaixo. 
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

print(dict(zip(dict1, dict2.values())))

# %%
# Exercício 10 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

L10 = list(map(lambda x: x[1], filter(lambda x: x[0] > 5, enumerate(lista))))

# Ou, obviamente, L10 = lista[5 + 1:]

print(L10)

# %%
