#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi aludado. Calcule o preço a pagar, sabendo que o carro custa R$ 60.00 por dia e R$ 0.15 por KM rodado.

n1 = float(input('Quantos KM você percorreu com o carro?'))
n2 = float(input('Quantos dias você ficou com o carro alugado?'))
n3 = n1 * 0.15
n4 = n2 * 60
print('o carro percorreu {:.2f}KM, e ficou com carro {:.2f} dias'.format(n1, n2))
print('O valor total apagar por dia {:.2f}, e qual valor total em KM rodados R${:.2f}'.format(n3, n4))

