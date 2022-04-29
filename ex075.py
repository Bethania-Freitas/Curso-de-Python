tupla = (int(input('Digite um numero: ')),
         int(input('Digite outro numero: ')),
         int(input('Digite mais um numero: ')),
         int(input('Digite o último numero numero: ')))

print('=-'*20)
print(f'Você digitou os valores{tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vez(es)')
if 3 in tupla:
    print(f'O numero 3 apareceu na posição {tupla.index(3)+1}')
else:
    print(f'O numero 3 não foi digitado')
print(f'Os valores pares digitados foram ', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end='  ')



