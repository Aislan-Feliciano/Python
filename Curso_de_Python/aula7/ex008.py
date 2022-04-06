#Ler um valor em metros e o exiba convertido em centimetros e milimetros.#
num = float(input('Digite um numero:'))
c1 = num * 100
m1 = num * 1000
print('O numero digitado é {:.0f}, convertendo para centimetro {:.0f} e para milimetro {:.0f}.'.format(num, c1, m1))