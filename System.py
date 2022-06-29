# Sistema de ajuda em Python
from time import sleep 
# Cores que podem ser utilizadas no título do sistema, caso deseje pode adicionar mais cores. 
cor = (
'\033[m', #0 - Sem cor 
'\033[0;30;41m', #1 - Vermelho
'\033[0;30;42m', #2 - Verde
'\033[0;30;43m', #4 - Azul
'\033[0;30;44m', #5 - Roxo
'\033[7;30m',    #6 - Branco
'\033[1;30m',    #7 - Preto
);
def ajuda(comando):
    título(f'Acessando o manual do comando \'{comando}\'', )
    #print(cor[6], end='')
    help(comando)
    #print(cor[0], end='')
    sleep(2)

def título(msg, cor=0):
    tamanho = len(msg) + 4
    print('—' * tamanho)
    print(f'  {msg}')
    print('—' * tamanho)
    #print(cor[0], end='')
    sleep(1)

# Programa principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PYHELP', )
    comando = str(input('Qual Função ou Biblioteca gostaria de ver? '))
    if comando.upper() == 'Sair':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', )
