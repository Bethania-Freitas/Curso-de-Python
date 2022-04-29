n1 = float(input('Qual comprimento da reta 1: '))
n2 = float(input('Qual o comprimento da reta 2: '))
n3 = float(input('Qual o comprimento da reta 3: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('\033[32m Forma um triagulo')
else:
    print('\033[31m Não forma um triangulo')


