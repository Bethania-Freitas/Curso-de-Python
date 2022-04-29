lnome = []
lidade = []
lsexo = []
for c in range (1, 5):
    print('====== {}ª Pessoa ====='.format(c))

    nome = str(input('Nome: ')).title()
    lnome.append(nome)

    idade = int(input('Idade: '))
    lidade.append(idade)

    sexo = str(input('Sexo [M\F]: ')).upper()
    lsexo.append(sexo)

a = 0
for l in lidade:
    a += l
mediaidade = a / 4
print('A media de idade do grupo é de {:.0f}'.format(mediaidade))
m = max(lidade)
for k, v in enumerate(lidade):
    if v == m:
        if lsexo[k] == 'F':
            print('A mulher mais velha tem {} anos e se chama {}'.format(lidade[k],lnome[k]))
        else:
            print('O homem mais velho tem {} anos e se chama {}'.format(lidade[k], lnome[k]))
mulher = 0
for k, v in enumerate(lsexo):
    if v == 'F' and lidade[k] < 20:
        mulher = mulher+1
if mulher > 0:
    print('Ao todo são {} mulheres abaixo de 20 anos'.format(mulher))
else:
    print('Não há mulheres abaixo dos 20 anos')








