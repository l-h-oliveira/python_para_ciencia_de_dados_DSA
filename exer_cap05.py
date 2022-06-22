# %%
# Exercício 1 - Crie um objeto a partir da classe abaixo, chamado roc1, passando 2 parâmetros e depois faça uma chamada
# aos atributos e métodos
from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)

roc1 = Rocket(2,3)

print(roc1.x)
print(roc1.y)

roc1.move_rocket(2,4)

roc1.print_rocket()

# %%
# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

class Pessoa():

    def __init__(self, nome, idade, cidade, telefone, email):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.telefone = telefone
        self.email = email

    def mudanca_cid(self, cidade_nova):
        self.cidade = cidade_nova
    
    def aniversario(self):
        self.idade += 1

    def novo_email(self, novo_email)        :
        self.email = novo_email

lucas = Pessoa('Lucas', 29, 'Sain Julien', '123456789', 'lucas@lucas.com')

print(lucas.email)
lucas.novo_email('lucas@gmail.com')
print(lucas.email)

print(lucas.idade)
lucas.aniversario()
print(lucas.idade)

# %%
# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class Smartphone():
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface

class MP3player(Smartphone):
    def __init__(self, tamanho, interface, capacidade):
        Smartphone.__init__(self, tamanho, interface)
        self.capacidade = capacidade

iphone = Smartphone('12cm', 'ios') 
print(iphone.tamanho, iphone.interface)

mplayer = MP3player('5cm', 'simples', '2MB')
print(mplayer.tamanho, mplayer.interface, mplayer.capacidade)

# %%
