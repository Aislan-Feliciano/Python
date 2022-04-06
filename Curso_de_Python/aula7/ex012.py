#Ler um preço de um produto e mostre seu novo preço. Com 5% desconto.#

n1 = float(input('Qual é valor dessa camisa?'))
n2 = (n1 * 5/100)
print('O valor real da camisa é R${:.2f} e valor da camisa com desconto {:.2f}'.format(n1, n2))