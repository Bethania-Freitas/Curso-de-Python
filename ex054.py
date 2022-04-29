adu = 0
jov = 0
for a in range(1,7):
    n = int(input('Digite o ano de nascimento da {} pessoa: '.format(a)))
    if n <= 2004:
        adu = adu + 1
    else:
        jov = jov + 1
print('Ao todo tivermos {} maiores de idade'.format(adu))
print('E também temos {} menores de idade'.format(jov))

