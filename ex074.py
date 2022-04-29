from random import randint
tupla = (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),)
print(f'Os valores sorteados foram ',end=' ')
for n in tupla:
    print(f'{n} ',end=' ')


#ASSIM FOI COMO EU CHEGUEI NO RESULTADO
#nova = sorted(tupla)
#print(f'O maior valor é {nova[4]}')
#print(f'O menor valor é {nova[0]}')

#ASSIM FOI COMO ELE CHEGOU
print(f'\nO maior valor é {max(tupla)}')
print(f'O menor valor é {min(tupla)}')



