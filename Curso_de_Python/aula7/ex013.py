#Ler um salário de funcionário e mostre seu novo salário com 15% de aumento.#

n1 = float(input('Qual é o valor do seu salario?'))
n2 = ((n1 * 15/100) + n1)
print('salario atual R${}, salario com aumento R${}'.format(n1, n2))



