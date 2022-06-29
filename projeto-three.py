# Decida por mim - nesse projeto vc irá fazer uma pergunta e o sistema irá retornar uma resposta com base em uma lista com as possíveis respostas de forma aleátoria.
# Momento em que o usuário fara alguma pergunta.
from time import sleep
import random 
print('Me faça uma pergunta abaixo ⬇️')
sleep(1.5)
pergunta = str(input('Pergunte: '))
# Aqui será quando o computador vai escolher uma resposta aleátoria dentro da lista.
#file = open('lista-resposta.txt')
lista = ["Não sei ué.", "Você quem sabe.", "Claro, vai que acontece algo legal.", "Acho melhor não.", "Você tem dinheiro pra isso?"]
elemento = random.choice(lista) #Computador ira fazer a escolha de uma resposta dentro da lista de forma aleatoria.
for x in 'lista':
    print(elemento)
    break
