soma = 0
cont = 0
for c in range (6):
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('Voce informou {} numeros pares e a soma deles é de  {}'.format(cont, soma))



