from datetime import date
ano = int(input('Qual o ano de nascimento: '))
idade = date.today().year - ano
print('Você tem {} anos'.format(idade))

if idade == 18:
    print('Este é o ano certo para seu alistamento!')
elif idade < 18:
    print('Ainda faltam {} para seu alistamento'.format(18-idade))
else:
    print('Já passou {} do seu alistamento'.format(idade-18))