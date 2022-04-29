print('Super progressão aritmética')
print('=-' *20)

PA = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = razao*10 + PA
conta = 1
for conta in range(PA,termo,razao):
    print('{} -> '.format(conta),end=' ')
    conta += 1

print('PAUSA')
PA2 = 1
cont = PA2
while PA2 != 0:
    PA2 = int(input('Quantos termos você quer mostrar a mais: '))
    if PA2 > 0:
        conta2 = 1
        while conta2 <= PA2:
            print('{} -> '.format(termo),end=' ')
            termo += razao
            conta2 += 1
        print('PAUSA')
        cont += PA2
print('Progressão finalizada com {} termos mostrados'.format(cont + 9))

