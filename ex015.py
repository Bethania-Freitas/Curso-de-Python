a=int(input('Por quantos dias o carro ficou alugado: '))
b=float(input('Qual a kilometragem que foi rodada:'))
c=(a*60)+(b*0.15)
print('O total a pagar por {} dias rodados com {} km é de R$ {:.2f}'.format(a, b, c))



