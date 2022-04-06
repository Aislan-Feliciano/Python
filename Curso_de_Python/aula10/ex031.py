'''Desenvolva um programa que pergunta a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de ate 200km e R$ 0.45 para viagens mais longa.'''

dist = float(input('Qual foi a distância que você percorreu na viagem? Km'))
preço = 0.50 * dist
if dist <= 200:
    print('O preço da passagem será R${:.2f} até 200Km'.format(preço))
else:
    print('O preço da viagem mais longa será R${:.2f}'.format(0.45 * dist))
#preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45: outra forma de fazer!