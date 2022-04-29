qtde = soma = n = 0
while True:
    n = int(input('Digite um numero, ou 999 para parar: '))
    if n == 999:
        break
    soma += n
    qtde += 1
print(f'Você digitou {qtde} numeros que somam {soma}')
