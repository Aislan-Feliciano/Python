'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

n1 = int(input('digite um numero:'))
n2 = int(input('digite outro numero:'))
n3 = int(input('digite outro numero:'))
if n1 > n2 and n2 < n3:
    print('Se o número {}, for maior que {} e menor que numero {}!'.format(n1, n2, n3))
'''else:
    print('o número {}, é menor que numero anterior {}?'.format( n2, n4))'''