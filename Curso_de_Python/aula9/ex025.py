'''crie um programa que lei o nome de uma pessoa e diga se ela tem SILVA nome'''
nome = str(input('digite o nome de uma pessoa:')).strip()
n1 = 'SILVA' in nome.upper()
print('analisando o nome {}'.format(nome))
print('Seu sobre nome tem ou não Silva? {}'.format(n1))

