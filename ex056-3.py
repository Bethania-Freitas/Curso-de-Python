somaidade = 0
mediaidade = 0
hmaisvelho = 0
nomevelho = ''
mulher20 = 0
for c in range(1, 5):
    print('======{}ª Pessoa ======'.format(c))
    nome = str(input('NOME: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M\F]: ' )).strip().upper()
    somaidade += idade
    if sexo == 'M' and idade > hmaisvelho:
        hmaisvelho = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulher20 += 1



mediaidade = somaidade / 4

print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} e se chama {}'.format(hmaisvelho, nomevelho))
print('Ao todos são {} mulheres menores de 20 anos'.format(mulher20))

