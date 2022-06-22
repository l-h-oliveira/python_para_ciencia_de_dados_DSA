# %%
# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
L = []
for i in range(10):
    L.append(i + 1)
    print(i + 1)

print(L)    
# %%
# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela

L = ['a', 5, 'bom', 3, (2,3), [1,2,]]

for x in L:
    print(x)

# %%
# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string

a1 = 'Bom'
a2 = ' Dia!'

a3 = a1 + a2

print(a3)

# %%
# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do  objeto tupla para verificar quantas vezes o número 4 aparece na tupla

T = (1, 2, 2, 3, 4, 4, 4, 5)

u = T.count(4)

print(u)

# %%
# Exercício 5 - Crie um dicionário vazio e imprima na tela

d = {}

print(d)
print(type(d))

# %%
# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela

d = {'uva':'fruta', 'caneta': 'objeto', 'garfo': 'talher'}

print(d)

for x in d.keys():
    print('{0} --> {1}'.format(x, d[x]))

# %%
# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela

d.update({'leite': 'bebida'})

print(d)

# %%
# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e o quarto elemento um valor do tipo float. Imprima a lista na tela.

L = ['tau', (1,2), {'uva':'fruta', 'caneta': 'objeto'}, 2.718]

for x in L:
    print('{0} ---> {1}'.format(x, type(x)))

# %%
# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.

frase = 'Cientista de Dados é o profissional mais sexy do século XXI'

print(frase[0:18])

