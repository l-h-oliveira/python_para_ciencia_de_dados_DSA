# %%
from random import choice


def escolher_palavra():
    with open('palavras.txt') as file:
        palavras = file.readlines()

    return choice(palavras).replace('\n', '')
# %%
man_fig = ['''*****************
   ______
  |      |
         |
         |
         |
         |
******************\n
''', '''*****************
   ______
  |      |
  o      |
         |
         |
         |
******************\n
''', '''*****************
   ______
  |      |
  o      |
  |      |
         |
         |
*****************\n
''', '''*****************
   ______
  |      |
  o      |
 /|      |
         |
         |
******************\n
''', '''*****************
   ______
  |      |
  o      |
 /|\     |
         |
         |
******************\n
''', '''*****************
   ______
  |      |
  o      |
 /|\     |
 /       |
         |
******************\n
''', '''*****************
   ______
  |      |
  o      |
 /|\     |
 / \     |
         |
******************\n
''']

# %%
class HangMan:
    def __init__(self, word):
        self.word =  word

        # # o status do jogo começa com todas letras ocultadas
        # self.status = len(word)*'-'
        
        # contador de estágirdos da forca, o jogo termina quando chega a 6
        self.counter = 0 

        # Lista de palpites acertados
        self.corrects = []

    # Método para verificar o status do game
    def game_status(self):
        a = self.word
        for x in self.word:
            if not (x in self.corrects):
                a = a.replace(x, '-')        
        print('     ', a, '\n', man_fig[self.counter])

    # Método para fazer uma tentativa de letra
    def try_letter(self, l):
        if l in self.word:
            self.corrects.append(l)
            print('A palavra possui letra(s) {}'.format(l))
        else:
            self.counter += 1
            print('A palavra não possui letra(s) {}'.format(l))

    # Método que verifica se o jogo acabou
    def game_over(self):
        if self.counter == 6:
            print('O jogo acabou!')
            return True
        else:
            return False

    # Método para fazer um palpite de palavra
    def make_guess(self, w):
        if w == self.word:
            print('Você venceu!!! Parabéns!!! Agora, vá estudar!')
        else:
            print('Você perdeu!" \n A palavra é {}. \n Agora, vá estudar!'.format(self.word))    

# Instanciando o objeto do jogo
forca = HangMan(escolher_palavra())

# %%
print('\n \n ####### Joguinho da Palavra ####### \n ')

while (not forca.game_over()):
    #início do jogo
    forca.game_status()
     
    # Palpite de uma letra
    l = input('Tente uma letra: ')
    forca.try_letter(l)

    # Verificando o status do jogo
    forca.game_status()

    # Verificando se o jogador quer dar um palpite da palavra
    p = input('Adivinhou a palavra? [s/N] ')
    if (p.lower() == 's'):
       p = input('Qual é a palavra? ')
       forca.make_guess(p)
       break

# %%
