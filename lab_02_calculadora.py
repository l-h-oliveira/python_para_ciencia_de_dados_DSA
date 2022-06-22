# %% Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator ******************* \n")

intro = 'Selecione o número da operação desejada: \n \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n'

print(intro)

op = input('Digite sua opção (1, 2, 3, 4): ')

# %%
while op not in ['1','2','3','4']:
    print('\nOpção Inválida!')
    op = input('Digite sua opção (1, 2, 3, 4): ')
# %%
ops = {'1': 'Soma', '2': 'Subtração', '3': 'Multiplicação', '4': 'Divisão'}

print('\n{0} selecionada!'.format(ops[op]))

x = float(input('\nDigite o primeiro número: '))
y = float(input('\nDigite o segundo número: '))

while (y == 0 and op == '4'):
    print('\nNão podemos dividir por zero!')
    y = float(input('Digite um segundo número valído: '))

if op == '1':
    print('{0} + {1} = {2}'.format(x, y, x + y))
elif op == '2':
    print('{0} - {1} = {2}'.format(x, y, x - y))
elif op == '3':
    print('{0} * {1} = {2}'.format(x, y, x*y))        
else:
    print('{0} / {1} = {2}'.format(x, y, x/y)) 