# %%
# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

dia = input('Qual o dia da semana? \n').lower()

if (dia == 'domingo' or dia == 'sábado'):
    print("Hoje é dia de descanso.")
else:
    print("Você precisa trabalhar!")    

# %%
# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

frutas = ['banana', 'uva', 'maçã', 'morango', 'abacaxi']

if 'morango' in frutas:
    print('Faz morango faz parte da lista.')
else:
    print('Faz não morango faz parte da lista.')    

# %%
# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma lista

T3 = (1, 3, 6, 7)
L3 = []
for x in T3:
    L3.append(2*x)

print(L3)    

# %%
# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela

L4 = list(range(100, 151, 2))

print(L4)

# %%
# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, imprima as temperaturas na tela

temperatura = 40

while temperatura > 35:
    print(temperatura)

# %%
# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela, mas quando for encontrado o valor 23, interrompa a execução do programa

contador = 0

while contador < 100:
    print(contador)
    if contador == 23:
        break
    contador += 1

# %%
# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, adicione à lista, apenas os valores pares e imprima a lista

L7 = []
a7 = 4

while (a7 <= 20):
    L7.append(a7)

    a7 += 1

print(L7)

# %%
# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
nums = range(5, 45, 2)

L8 = list(nums)

print(L8)

print(type(L8))

# %%
# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.

temperatura = float(input('Qual a temperatura? '))
if temperatura > 30: # faltou ':'
    print('Vista roupas leves.') #concatenação
else: #faltou ':
    print('Busque seus casacos.')

# %%
# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na sua instrução de impressão

frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir." 

c = 0

for x in frase:
    if x == 'r':
        c += 1

print('Na frase: "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."  há {} letras r.'.format(c))        

# ou

c = frase.count('r')
# %%
