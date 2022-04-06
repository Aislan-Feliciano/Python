#crie um programa que lei um numero real qualquer pelo teclado mostre na tela a sua porcão interira:
import math

n1 = float(input('Digite um número:'))
n2 = math.trunc(n1)
print('o número real {}, é uma porção inteira {}'.format(n1, n2))
