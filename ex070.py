print('='*30)
print('SALDAO DA ECONOMIA')
print('='*30)

total = mil = prebarato = compra = preço = 0

while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: R$  '))
    sn = str(input('Deseja cadastrar mais compras [S/N]: ')).upper().strip()[0]
    print('-'*30)
    total += preço
    compra += 1
    if compra == 1:
        probarato = produto
        prebarato = preço
    else:
        if preço < prebarato:
            probarato = produto
            prebarato = preço

    if preço > 1000:
        mil += 1
    if sn == 'N':
        break

print(f'Você fez {compra} compras no total de R$ {total:.2f}')
print(f'Foi feito {mil} compra acima de R$ 1000.00')
print(f'O produto mais barato foi {probarato} que custou R$ {prebarato:.2f}')

