print('='*20)
print ('10 termos de uma PA')
print('='*20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
conta = 1
while conta <= 10:
    print('{} -> '.format(termo),end=' ')
    termo += razao
    conta += 1
