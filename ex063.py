print('======= Sequencia de Fibonacci=======')
termos = int(input('Quantos termos você quer mostrar?  '))
n1 = 0
n2 = 1
n3 = n1 + n2
progressao = 0
while progressao < termos:
    progressao += 1
    print('{} ->'.format(n1),end=" ")
    n1 = n2
    n2 = n3
    n3 = n1 + n2
print('FIM')



