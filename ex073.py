tupla = ('Atlético', 'Botafogo', 'Flamengo', 'Corintians', 'Coritiba',
         'Goias', 'Palmeiras', 'Ceara', 'Fortaleza', 'Cuiaba', 'Avai',
         'America', 'São Paulo', 'Internacional', 'Juventudi',
         'Bragantino', 'Fluminence', 'Santos')
print('='*40)
print(f'Os times do Brasileirão 2022 são: {tupla}')
print('='*40)
print(f'Os primeiros 5 são: {tupla[:5]}')
print('='*40)
print(f'Os cinco últimos são: {tupla[-5:]}')
print('='*40)
print(f'Os times em ordem alfabetica são:{sorted(tupla)}')
print('='*40)
print(f'O Ceara esta na posição: {tupla.index("Ceara")+1}')

