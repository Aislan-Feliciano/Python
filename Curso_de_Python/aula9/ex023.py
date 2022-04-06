'''Faça um programa que leia um numero de 0 a 9999 e mostra na tabela cada um dos digitos separados.
ex: digite um numero: 1834
unidade:4
dezena:3
centena:8
milhar:1'''
'''num = int(input('Digite um numero:'))
n = str(num)
print('Analisando o numero {}:'.format(num))
print('A unidade desse numero é {}'.format(n[3]))
print('A dezena desse numero é {}'.format(n[2]))
print('A centena desse numero é {}'.format(n[1]))
print('A unidade milhar desse numero é {}'.format(n[0]))'''

num = int(input('Digite um numero:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('A nalisando o numero {}'.format(num))
print('unidade {}'.format(u))
print('dezena {}'.format(d))
print('centena {}'.format(c))
print('unidade milhar {}'.format(m))