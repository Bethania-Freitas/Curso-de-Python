resp = 'S'
qtde = media = soma = maior = menor = 0
while resp in 'sS':
    num = int(input('Digite um numero: '))
    qtde += 1
    soma += num
    if qtde == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

    resp = str(input(('Quer continuar? [S/N]'))).upper().strip()[0]
media = soma/qtde
print('Você digitou {} numeros e a Média entre eles é de {}'.format(qtde, media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))