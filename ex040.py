m1 = float(input('Qual nota da primeira prova: '))
m2 = float(input('Qual a média da segunda nota: '))
m3 = (m1 + m2) / 2

if m3 < 5:
    print( 'Sua média foi de {:.1f}, você esta REPROVADO'.format(m3))
elif m3 >= 5 and m3 <= 6.9 :
    print('Sua média foi de {:.1f}, você esta de RECUPERAÇÃO'.format(m3))
else:
    print('Sua média foi de {:.1f}, você esta APROVADO'.format(m3))
