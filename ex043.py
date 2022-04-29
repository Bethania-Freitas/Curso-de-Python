al = float(input('Qual a sua altura: '))
peso = float(input('Qual é seu peso: '))

icm = peso / (al**2)

if icm < 18.5:
    print ('O seu ICM é de {:.2f}, você esta \033[1;32mabaixo do peso'.format(icm))
elif icm >= 18.5 and icm < 25:
    print('O seu ICM é de {:.2f}, você esta no \033[1;33mpeso ideal'.format(icm))
elif icm >= 25 and icm < 30:
    print('O seu ICM é de {:.2f}, você esta com \033[1;34msobrepeso'.format(icm))
elif icm >= 30 and icm < 40:
    print('O seu ICM é de {:.2f}, você esta com \033[1;35mobesidade'.format(icm))
else:
    print('O seu ICM é de {:.2f}, você tem obesidade \33[1;31mmormida')

