from datetime import date
ano = int(input('Qual o ano de nascimento do atleta: '))
idade = date.today().year - ano

if idade < 9:
    print('O atleta tem {} anos e vai entrar na categoria MIRIM'.format(idade))
elif idade >= 9 and idade < 14:
    print('O atleta tem {} anos e vai entrar na categoria INFANTIL'.format(idade))
elif idade >= 14 and idade <= 19:
    print('O atleta tem {} anos e vai entrar na categoria JUNIOR'.format(idade))
elif idade == 20:
    print('O atleta tem {} anos e vai entrar na categoria SENIOR'.format(idade))
else:
    print('O atleta tem {} anos e vai entrar na categoria MASTER'.format(idade))
