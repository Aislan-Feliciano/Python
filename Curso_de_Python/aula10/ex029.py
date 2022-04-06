'''Escreva um programa e lei a velocidade de uma carro:
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7.00 por cada km acima do limite.'''
vel = float(input('Qual foi a velocidade que esse carro atingiu?'))
if vel > 80:
    print('seu carro foi multado!')
    mul = (vel - 80) * 7
    print('O valor da multado é R${:.2f}!'.format(mul))
print(' Seu carro não foi multado, pode seguir!')