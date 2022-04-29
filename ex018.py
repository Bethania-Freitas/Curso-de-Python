import math
n=float(input('Informe o grau:'))
cos= math.cos(math.radians(n))
seno= math.sin(math.radians(n))
tan= math.tan(math.radians(n))
print("O valor de seno é {:.2f} e de cosseno é {:.2f} e a tangente é {:.2f}".format(seno,cos, tan))
