sal = input('Digite o valor do salario do funcionario: R$ ').replace(',','.')
sal2 = float(sal)
if sal2 > 1250.00:

    #COMO EU FIZ...
#    print('O salario que era de R$ {:.2f} vai ter reajuste de 10% passando a ser: R$ {:.2f}'.format(sal2,(sal2*10/100)+sal2))
#else:
#    print('O salario que era de R$ {:.2f}, teve reajuste de 15% passando a ser de: R$ {:.2f}'.format(sal2,(sal2*15/100)+sal2))

    #COMO O PROF FEZ:
    sal3 = sal2 + (sal2 * 10 / 100)
else:
    sal3 = sal2 + (sal2 * 15 /100)
print ('Quem ganhava \033[1;45m R$ {:.2f}\033[m, vai passar a ganhar \033[1;45m R$ {:.2f}\033[m'.format(sal2, sal3))
