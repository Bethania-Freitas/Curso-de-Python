import math
n=float(input('Qual o comprimento do cateto oposto: '))
n2=float(input('Qual o comprimeiro do cateto adjacente: '))
n3=math.hypot(n,n2)
print('A soma de {} com {} da o valor {:.2f} para hipotenusa'.format(n,n2,n3))
