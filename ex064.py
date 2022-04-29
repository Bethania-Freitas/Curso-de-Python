soma = 0
cont = 0
n = 0
n = int(input('Digite um numero para somar ou 999 para parar: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um numero para somar ou 999 para parar: '))
print('Você digitou {} numeros que somam {}'.format(cont, soma))

