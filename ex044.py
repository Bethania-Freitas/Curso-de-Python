print('{:=^40}'.format('JUSTA MUSIC'))

p = float(input('Qual o preço final da compra: R$ '))
print('Escolha abaixo qual a forma de pagamento:')
print('''1 - à vista em dinheiro\cheque
2 - à vista no cartão
3 - 2x no cartão'
4 - 3x ou mais no cartão''')
pgto = int(input())
if pgto == 1:
    print('A sua compra de R$ \033[1;33m{}\033[m, vai sair por R$ \033[1;34m{}'.format(p, p-(p*10/100)))
elif pgto == 2:
    print('A sua compra de R$ \033[1;33m{}\033[m, vai sair por R$ \033[1;34m{}'.format(p, p-(p*5/100)))
elif pgto == 3:
    print('A sua compra de R$ \033[1;33m{}\033[m, vai ficar em 2x de R$ \033[1;34m{}'.format(p,p/2))
elif pgto == 4:
    par = int(input('Quantas parcelas: '))
    print(' A sua compra de {}, vai ficar em {} parcelas de {}'.format(p,par,(p+(p*20/100))/par))
else:
    print('forma de pagamento não reconhecida')
