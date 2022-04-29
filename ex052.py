soma = 0
n = int(input('Digite um numero '))
for c in range (1, n+1):
    print(c, end=' ')
    if n % c == 0:
        soma = soma + 1
print('\nO numero {} é divisivel nesta PA {} vezes'.format(n, soma))
if soma == 2:
    print('O numero {} é um numero PRIMO'.format(n))
elif soma == 1:
    print('O numero {} é um numero NATURAL'.format(n))
else:
    print('O numero {} NÂO é um numero primo'.format(n))









