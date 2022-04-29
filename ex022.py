nome = str(input('Qual o seu nome: ')).strip()
print('Nome: {}'.format(nome.upper()))
print('Nome minusculo: {}'.format(nome.lower()))
print('Qtde de caracteres:{}'.format(len(nome)-nome.count(' ')))
nome2 = nome.split()
print('O primeiro nome tem {} caracteres'.format((len(nome2[0]))))


