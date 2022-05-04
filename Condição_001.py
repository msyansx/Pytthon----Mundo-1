print("JOGO DA ADIVINHAÇÃO 1.0")

from random import randint 
from time import sleep

pc = randint(0, 5)

print('=' * 20)
print("Vou pensar em um número de 0 a 5")
print("Tenta adivinhar o número que eu pensei...")
print('=' * 20)

player = int(input("Em que número eu pensei?: "))
print("Processando...")
sleep(2)

if player == pc:
    print("Parabéns você conseguiu me vencer!") 

else: 
    print("Ganhei! Eu pensei no número {} e não no {}.".format(pc, player))