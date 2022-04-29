tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze','quatorze','quinze', 'dezesseis','dezesete','dezoito','dezenovo','vinte')
cont = ''

while True:
    c = int(input('Escreva um numero entre 0 e 20: ' ))
    if 0 <= c <= 20:
        break
print(f'Você digitou o numero {tupla[c]}')
cont = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
while cont in 'Ss':
    while True:
        c = int(input('Escreva um numero entre 0 e 20: '))
        if 0 <= c <= 20:
            break
    print(f'Você digitou o numero {tupla[c]}')
    cont = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
print('FINALIZADO')



