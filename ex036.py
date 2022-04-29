casa = float(input('Qual o valor da imovel: R$ '))
sal = float(input('Qual o valor do seu salario: R$ '))
anos = int(input('Em quantos anos deseja quitar o emprestimo: '))

fin = casa / (anos * 12)
sal2 = (sal*30/100)
if fin <= sal2:
    print('Você vai pagar R$ {:.2f} mensais por {} anos'.format(fin,anos))
else:
    print('Infelizmente não podemos conceder o emprestimo nestas condições')