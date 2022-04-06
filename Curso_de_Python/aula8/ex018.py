#faça um programa que leia um angulo qualquer e mostre na tela o valor de seno, cos e tag desse angulo.

'''import math
angulo = float(input('digite o angulo que você deseja:'))
seno = math.sin(math.radians(angulo))
print('O angulo de {} , tem seno de {}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('o angulo de {}, tem cosseno de {}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('o angulo de {}, tem tangente de {}'.format(angulo, tangente))'''
from math import radians, sin, cos, tan
angulo = float(input(' digite o angulo que você deseja:'))
seno = sin(radians(angulo))
print('O angulo de {} , tem seno de {}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('o angulo de {}, tem cosseno de {}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('o angulo de {}, tem tangente de {}'.format(angulo, tangente))