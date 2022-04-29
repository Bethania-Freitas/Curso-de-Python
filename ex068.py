from random import randint
print('VAMOS JOGAR PAR OU IMPAR?')
print('='*20)

soma = jogada = vitoria = 0
while True:
    n = int(input('Escolha seu numero: '))
    pi = str(input('Escolha PAR ou IMPAR [P/I]')).upper().strip()[0]
    print('-'*20)
    comp = randint(0,10)
    soma = comp + n
    jogada += 1
    if soma % 2 == 0:
        if pi == 'P':
            print(f'O computador escolheu {comp} e você {n}. A soma é {soma} - PAR')
            print('Você ganhou!!   Vamos jogar novamente....')
            vitoria += 1
        else:
            print(f'O computador escolheu {comp} e você {n}. A soma é {soma} - PAR')
            break
    else:
        if pi == 'I':
            print(f'O computador escolheu {comp} e você {n}. A soma é {soma} - IMPAR')
            print('Você ganhou!!   Vamos jogar novamente....')
            vitoria += 1
        else:
            print(f'O computador escolheu {comp} e você {n}. A soma é {soma} - IMPAR')
            break
print('Você perdeu')
print(f'Game over. De {jogada} jogadas. Você ganhou {vitoria} vezes')



