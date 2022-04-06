'''Crie um programa que lei o nome completo de uma pessoa e mostre:
 O nome com todas as letras maiusculas:
 O nome com todas as letras minusculas:
 Quantas letras ao todo (sem considera o espaço):
 Quantas letras tem o primeiro nome:'''

'''nome = str(input('Qual é seu nome completo?'))
n1 = nome.upper()
n2 = nome.lower()
n3 = len(nome.strip())
n4 = nome [:7]
print(n1, n2, n3,n4 )'''

nome = str(input('Qual é seu nome completo?')).strip()
print('analisando seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome todo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
#separa = nome.split()
#print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))
#count(' ') vai contar quanto espaço vai ter, espaço nas aspas "(' ')"
