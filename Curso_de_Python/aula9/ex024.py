'''Crie um progrma que lei o nome de uma cidade e diga se ela começa ou não com nome SANTO'''
cidade = str(input('Digite o um nome de uma cidade:')).strip()
n1 = cidade[:5].upper() == 'SANTO'
#print('A analisando o nome da cidade {} \n a cidade começa ou não o nome: {}'.format(cidade, n1))

print(n1)