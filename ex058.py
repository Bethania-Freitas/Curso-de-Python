#from random import randint
#comp = randint(0, 10)
#Humano = 0
#print('Vamos jogar um jogo de adivinha!\nEu vou pensar num numero e vc tenta adivinhar qual é!')
#while Humano != comp:
#    Humano = int(input('Fale um numero de 0 a 10: '))
#    if Humano < comp:
#        print('Mais... tente novamente!')
#    else:
#        print('Menos... tente novamente')
#    print(' ')
#    Humano += 1
#print('Parabens!!!  Você acertou na {}ª tentativa'.format(Humano))


from random import randint
comp = randint(0,10)
print('Eu sou seu computador, e estou pensando em um numero de 0 a 10')
print('Consegue adivinhar qual é?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual o seu palpite: '))
    palpite += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print('Mais... tente novamente')
        else:
            print('Menos... tente novamente')
print('Você acertou em {} rodadas!!'.format(palpite))
