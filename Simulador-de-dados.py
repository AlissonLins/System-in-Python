#Simulador de Dados -
#Este simulador irá exibir na tela um valor entre os números 1 a 6
from random import randint
from time import sleep
computador = randint (1, 7) #Computador pensa em um número
print('Olá, Sou o seu computador... Acabei de pensar em um número. Dica: entre 1 e 6. ')
acertou = False
palpites= 0
while not acertou:
    jogador = int(input('Qual número eu pensei? ')) #Jogador tenta adivinhar o número pensado pelo computador.
    print('PROCESSANDO, AGUARDE...')
    sleep(1.5)
    palpites =+ 1
    #print(f'O computador jogou {computador}')
    print(f'O jogador jogou {jogador}')
    if jogador < computador:
        print('Tente um valor maior.')
    elif jogador > computador:
        print('Tente um valor menor...')
    elif jogador == computador:
        acertou = True
print(f'PARABÉNS 🥳 você ganhou, mas foram necessário {palpites} tentativas.')
