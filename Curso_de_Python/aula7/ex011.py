#Ler a largura e altura de uma parade em metros. Calcule sua área e quantidade de tinta necessária para pita-la.
# sabendo que cada litro de tinta pinta uma área de 2m².

n1 = float(input('largura da parede:'))
n2 =  float(input('altura da parede:'))
n3 = n1 * n2
n4 = n3 / 2
print('A altura da parede {}m e larguta da parede {}m, corresponde uma area de {}m² consegue pinta {}m²'.format(n1, n2, n3, n4))