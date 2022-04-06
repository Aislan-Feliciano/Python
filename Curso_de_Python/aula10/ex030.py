'''Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou ímpar.'''
num = int(input('Digite um número:'))
resultado = num % 2
if resultado == 0:
    print('Se o número for {} é par, PARABÉNS VOCÊ GANHOU!'.format(num))
else:
    print('Se o número for {} é impar, VOCÊ PERDEU!'.format(num))
