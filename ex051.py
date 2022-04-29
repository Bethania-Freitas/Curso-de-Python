print('='*20)
print ('10 termos de uma PA')
print('='*20)

PT = int(input('Primeiro termo: '))
RZ = int(input('Razão: '))
F = RZ*10 + PT
for pa in range(PT, F, RZ):
    print(pa, end=' ')

