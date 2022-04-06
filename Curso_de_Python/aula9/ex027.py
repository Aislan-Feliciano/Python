'''Faça um programa que leia o nome de uma pessoa, mostrando em seguida o primeiro e o último nome
separadamente:
Ex: Ana Maria de Souza
primeiro: Ana
ultimo: Souza'''
nome = str(input('digite seu nome:')).strip()
n1 = nome.split()
print('Seu primeiro nome é: {}'.format(n1[0]))
print('seu ultimo nome é: {}'.format(n1[len(n1) - 1]))

