idade = soma18 = homem = mulheres = total = 0
sexo = 'M'
while True:
    print('='*30)
    print('CADASTRO DE CLIENTE')
    idade = int(input('Qual a idade: '))
    sexo = str(input('Digite o sexo [M/F]')).upper().strip()[0]
    while sexo not in "MF":
        sexo = str(input('Digite o sexo [M/F]')).upper().strip()[0]
    total += 1
    sn = str(input('Cadastrar novo cliente? [S/N]')).upper().strip()[0]
    while sn not in 'SN':
        sn = str(input('Cadastrar novo cliente? [S/N]')).upper().strip()[0]
    if sexo == 'M':
        homem += 1
    if idade >= 18:
        soma18 += 1
    if sexo == 'M' and idade < 20:
        mulheres += 1
    if sn == 'N':
        break
print('='*30)
print('FIM DO PROGRAMA')
print(f'Total de {total} pessoas cadastradas')
print(f'Total de pessoas maiores de 18 anos é {soma18}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'Ao todo temos {mulheres} mulher(es) com menos de 20 anos')