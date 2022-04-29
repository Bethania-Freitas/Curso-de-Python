c3 = 1

c1 = int(input('Digite um valor: '))
c2 = int(input('Digite outro valor: '))

print(' ')
print('O que deseja fazer com estes numeros:')
print(' [1]Somar\n [2]Multiplicar\n [3]Saber o maior\n [4]Novos numeros\n [5]Sair do programa ')

while c3 != 5:
    c3 = int(input('Opção escolhida: '))
    if c3 == 1:
        print('Soma: {} + {} = {}'.format(c1, c2, c1 + c2))
    elif c3 == 2:
        print('Multiplicar: {} x {} = {}'.format(c1, c2, c1*c2))
    elif c3 == 3:
        if c2 > c1:
            print('O maior numero é {}'.format(c2))
        else:
            print('O maior numero é {}'.format(c1))
    elif c3 == 4:
        c1 = int(input('Digite um valor: '))
        c2 = int(input('Digite outro valor: '))
        print(' ')
        print('O que deseja fazer com estes numeros:')
        print(' [1]Somar\n [2]Multiplicar\n [3]Saber o maior\n [4]Novos numeros\n [5]Sair do programa ')
    elif c3 != 1 and c3 != 2 and c3 != 4 and c3 != 5:
        print('Opção inválida')

    print(' ')
print('Obrigado e volte sempre')


