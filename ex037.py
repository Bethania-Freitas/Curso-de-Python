n1 = int(input('Digite um numero inteiro: '))

print('Qual a base para conversão?')
print('Digite 1 para binário \nDigite 2 para octal \nDigite 3 para hexadecimal')
n2 = int(input())

if n2 == 1:
    print('Numero binario de {} é {}'.format(n1, bin(n1)[2:]))
elif n2 == 2:
    print('Numero Octal de {} é {}'.format(n1, oct(n1)[2:]))
elif n2 == 3:
    print('Numero Hexadecimal de {} é {}'.format(n1, hex(n1)[2:]))
