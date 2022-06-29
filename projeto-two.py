# Chute o número - este programa ira gerar um valor aleatorio entre 1 a 100
from time import sleep
from random import randint
computador = randint (1, 101) #computador pensando em um número.
print('Olá, sou o seu computador, Vamos jogar?')
print('Vou pensar em um número, tente adivinhar...')
sleep(1.5)
acertou = False
while not acertou:
    jogador = int(input('Em que número em pensei? ')) # Aqui é o momento em que o usuário tenta adivinhar o número escolhido pelo sistema.
    print('Analisando...')
    sleep(1.5)
    print(f'O jogador tentou → {jogador}')
    if jogador > computador :
        print('O seu palpite foi muito alto, tente um valor menor.')
    elif jogador < computador:
        print('O seu palpite foi muito baixo, tente um valor maior.')
    else:
        acertou = True
        print('Você acertou o seu palpite, PARABÉNS 🥳')