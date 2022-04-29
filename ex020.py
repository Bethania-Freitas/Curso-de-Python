import random
a = str(input('Nome do aluno 1: '))
b = str(input('Nome do aluno 2: '))
c = str(input('Nome do aluno 3: '))
d = str(input('Nome do aluno 4: '))
e = [a, b, c, d]
random.shuffle(e)
print('A ordem de apresentação do trabalho será: {}'.format(e))
