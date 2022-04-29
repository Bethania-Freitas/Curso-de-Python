km = input('Qual a distancia percorrida em Km: ').replace(',','.')
d = float(km)

#FORMA QUE EU FIZ, TBM TA CERTO, É SÓ UMA OPÇÃO:
#if d <= 200:
 #   print('Cada Km custou R$ 0,50, você vai gastar {:.2f} nesta viagem'.format(d*0.50))
#else:
#   print('Cada Km custou R$ 0,45, você vai gastar R$ {:.2f} nesta viagem.'.format(d*0.45))

#FORMA QUE O PROF FEZ:
if d <= 200:
    preço = d * 0.50
else:
    preço = d * 0.45
print('Sua viagem de {:.2f} Km tera o custo de R$ {:.2f}'.format(d,preço))


