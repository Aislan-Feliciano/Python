#Ler quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. U$$ 1 dolar = R$ 5.00. #
n1 = float(input('digite um valor'))
n2 = n1 / 5
print('Eu tenho R${:.0f} na carteira, posso compra ${:.0f}.'.format(n1, n2))