print('\033[34m===DETECTOR DE PALINDROMO===\033[m')
n = str(input('Digite uma frase: '))
n2 = n[::-1]
print('O inverso de {} é {}'.format(n,n2))
n = n.replace(' ', '')
n2 = n2.replace(' ','')
if n == n2:
    print('É um Palindromo')
else:
    print('Não é um Palindromo')


