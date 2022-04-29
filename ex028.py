#import random
#n = int(input('Adivinhe o numero que estou pensando de 1 a 5: ' ))
#s = [1, 2, 3, 4, 5]
#t = random.choice(s)
#if n == t:
#   print('Você acertou, eu também pensei no {}'.format(t))
#else:
#    print('Você errou, eu pensei no numero {}'.format(t))

from random import randint
from time import sleep
comp = randint(0, 5) #faz o computador pensar de 0 a 5
humano = int(input('Vou pensar num numero de 0 a 5, adivinha qual estou pensando:'))
print('VAMOS VER....')
sleep(2)
if humano == comp:
   print('Você acertou, eu também pensei no {}'.format(comp))
else:
    print('Você errou, eu pensei no numero {} e não no {}'.format(comp, humano))


