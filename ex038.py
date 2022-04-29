n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1 < n2:
    print('O valor de {} é menor que {}'.format(n1, n2))
elif n1 > n2:
    print('O valor de {} é maior que {}'.format(n1, n2))
else:
    print('Os numeros {} são iguais e tem o mesmo valor'.format (n1))
