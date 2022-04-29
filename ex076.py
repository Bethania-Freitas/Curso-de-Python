print('-='*20)
print(f'{"LISTA DE PREÇOS":^40}')
print('-='*20)

tupla = ('Caderno', 9.90, 'Fichario', 25.00, 'Caneta', 3.50, 'Borracha', 2.00,
      'Livro', 79.90, 'Estojo', 35.00, 'Canetinhas', 40.00, 'Regra', 1.50, 'Mochila', 120.00)
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}',end=' ')
    else:
        print(f'R$ {tupla[pos]:>6.2f}')
