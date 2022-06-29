# Jogo de Aventura de texto - jogo baseado em decisões.
from time import sleep
print('Olá, Vamos jogar um game de aventura...')
print('Esse game vai ser baseado nas suas decisões.')
print('Vamos começar...')
sleep(1.5)
# Opções de história para o jogador ⬇️
print('[ 1 ] Você se torna o(a) maior Assassino(a) de Adarland ')
print('[ 2 ] Você é o(a) herdeiro(a) perdido(a) da YAKUZA ')
print('[ 3 ] Você será o(a) maior espadachin do mundo.')
opção = int(input('Escolha uma opção: ')) # escolha da história desejada
if opção == 1:
    print('Para começar a sua jornada digite o nome do seu personagem abaixo. ⬇️')
    nome = str(input('Nome do personagem: ')).upper() # Escolha de nome do personagem
    print(f'O nome escolhido foi {nome}.')
    print(f'Você é uma criança muito nova com apenas 12 anos de idade chamado(a) de {nome}.')# Inicio da História
    print('Sem um lar para onde ir ou pessoas com quem ficar, você se encontra com um homem cujo o nome é Arobynn Hamel.')
    print('Ele o convida para se juntar a ele.')
    resposta = str(input('Deseja segui-lo? '))
    if resposta == 'sim':
        print('Voces seguem para a guilda dos assassinos onde Arobynn Hammel te apresenta o local e todos que moram lá.')
        print('Tornando-se o(a) protegido(a) e braço direito de Arobynn Hamel.')
        print('='*65)
        print('Alguns anos depois...')
        print('='*65)
        print('Arobynn Convoca uma reunião, onde você e outros 8 assassinos foram convocados para esta reunião.')
        print('Porém uma dessas cadeiras está vazia.')
        print('E você pergunta: - onde está o Ben?')
        print('Dentro da guilda o Ben era o mais próximo de um amigo que eu tenho.') # Pensamento do seu personagem
        print('E arobynn responde: - Ele foi assassinado.')
        print('- Não sabemos quem o assassinou nem mesmo o que ele estava fazendo lá.')
        print('Pelo Ben ser a pessoa mais proxíma de um amigo, você fica muito irritado com isso.')# Pensamento do seu personagem
        print('Questionando tanto arobynn como os outros assassinos presentes na reunião pela morte de seu amigo.')# Pensamento do seu personagem
        print('='*75)
        print('2 meses depois, três assasinos da guilda também são assassinados repentinamente e arobynn envia você e outro assassino em busca de um pirata famoso.')
        print('Arobynn diz para vocês que esse pirata é responsavel pela morte dos assassinos da guilda.')
        print('Você e o seu companheiro vão para cobrar esta divida.')
        print('Chegando lá você descobre que este pirata não é o responsavel pela morte dos assassinos da guilda e que você foi enviado para lá por  outra missão.')
        print('Sendo que esta missão vai de contra as seus ideais e condutas.')
        sleep(2)
    elif resposta == 'não':
        print('Fim')
    
#elif opção == 2:
    #print('Para começar a sua jornada digite o nome do seu personagem abaixo. ⬇️')
    #nome = str(input('Nome do personagem: '))

#elif opção == 3:
   # print('Para começar a sua jornada digite o nome do seu personagem abaixo. ⬇️')
    #nome = str(input('Nome do personagem: '))
