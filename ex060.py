print('======FATORIAL======\n'' ')
n = int(input('Digite um numero: '))
c = n
f = 1
print('O fatorial de {}! é'.format(n),end=' ')
while c > 0:
    print('{}'.format(c),end=' ')
    print(' x ' if c > 1 else ' = ',end=' ')
    f *= c
    c -= 1

print('{}'.format(f))
