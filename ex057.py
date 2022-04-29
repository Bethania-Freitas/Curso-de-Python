#n = 1
#while n != 'M' and n != 'F':
#    n = str(input('Qual seu sexo [M\F]: ')).upper().strip()[0]
#    if n != 'M' and n != 'F':
#        print('Valor Invalido')
#print('Obrigada')

sexo = str(input('Digite seu sexo [M\F]:  ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, tente novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))