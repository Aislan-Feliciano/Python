'''Escreva um programa que faça o computador 'pensar' em um numero inteiro entre 0 e 5 e peça para
o usuário tentar descobrir qual foi o numero escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou não.'''

from random import randint
from time import sleep
computador = randint(0 , 5) # Faz o computardor "pensar"
print('-=-' * 20)
print('Vou pensar em numero entre 0, 5. Tente adivinhar...')
print('-=-'* 20)
jogador = int(input('Em qual número eu pensei?')) # jogador tenta adivinhar!
print('PROESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! você consigo me vencer!')
else:
    print('GANHEI! Eu pensei no múmero {} e não no {}!'.format(computador, jogador))


'''num = int(input('digite qualquer numero entre 0 à 5:'))
if num <= 5:
    print('Você venceu')
else:
    print('Você perdeu')
if num > 5:
    print('Não existe esse valor!')'''

