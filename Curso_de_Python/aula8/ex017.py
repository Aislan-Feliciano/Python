#faça um programa leia o comprimento do cateto oposto e do cateto adjacente de um triâgulo. calcule
#e mostre o comprimento da hipotenusa retangulo.

'''co = float(input('comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adjacente'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format( hi))'''
import math
co = float(input('comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adjacente'))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format( hi))