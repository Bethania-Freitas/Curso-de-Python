while True:
    tab = int(input('Quer ver a tabuada de qual valor: '))
    if tab < 0:
        break
    for c in range(1,11):
        multi = c * tab
        print(tab, ' x ', c, ' = ', multi)
print(f'Programa tabuada finalizado')