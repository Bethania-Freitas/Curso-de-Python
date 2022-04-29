nome1 = str(input('Digite seu nome completo: ').strip())
nome2 = nome1.split()
print('Nome Completo: {}'.format(nome1))
print('Primeiro nome: {}'.format(nome2[0]))
#print('Ultimo nome: {}'.format(nome2.pop()))  - tbm funciona, fiz pesquisando google
print('Ultimo nome: {}'.format(nome2[len(nome2)-1]))



