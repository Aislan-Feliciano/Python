#Escreva um programa que converta uma tempertura digital em °C e converta para °F.#

c = float(input('informe a temperatura em °c:'))
f = 9 * c / 5 + 32
print('A temprratura de {} °c, corresponde a {} °f'.format(c, f))