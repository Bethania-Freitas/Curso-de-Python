carro = float(input('Qual a velocidade do carro? '))
if carro <= 80.0:
    print('Parabens continue andando dentro do limite!')
else:
    print('Você esta acima da velocidade permitida, sua multa é de R$ {:.2f}'.format((carro - 80) *7))



