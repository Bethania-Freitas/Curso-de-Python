from random import randint
from time import sleep
print('\033[1mTopa jogar Jokempô comigo??\033[m')
J = int(input(('Digite \033[1;31m1\033[m para Sim e \033[1;31m2\033[m para Não: ')))
if J == 1:
    print('='*40)
    print('Legal!!  Suas escolhas são:')
    print('\033[1m[ 0 ]\033[m - para \033[1;35mPEDRA\033[m')
    print('\033[1m[ 1 ]\033[m - para \033[1;35mPAPEL\033[m')
    print('\033[1m[ 2 ]\033[m - para \033[1;35mTESOURA\033[m')

    P = int(input('Faça sua escolha: '))
    L = ('PEDRA','PAPEL','TESOURA')
    C = randint(0, 2)

    sleep(0.5)
    print('\033[1;36mJO')
    sleep(0.5)
    print('\033[1;36mKEN')
    sleep(0.5)
    print('\033[1;36mPO\033[m')
    sleep(0.5)

    print('Eu escolhi {}'.format(L[C]))
    print('Você escolheu {}'.format(L[P]))

    if C == P:
        print('\033[1;35mEMPATAMOS\033[m')
    elif C == 0 and P == 2 or C == 1 and P == 0 or C == 2 and P == 1:
        print('\033[1;35mEU GANHEI\033[m')
    elif C == 0 and P == 1 or C == 1 and P == 2 or C == 2 and P == 0:
        print('\033[1;35mVOCÊ GANHOU!\033[m')


else:
    print('Tudo bem, fica para proxima')
