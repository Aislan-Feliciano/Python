#Trabalhando com módulos:
# import doce (vai importa todos os doces)
# from doce import(só vai import um doce específico que você desajar)
# math significa matemática (vai importar tudo)
# ceil = arredonda pra cima
# floor = arredonda pra baixo
# trunc = elimina a virgula para frente
# pow = potencia
# sqrt = calcula raiz quadrada
# factorial = calcula fator equatorial
# hipot = calcula hipotenusa
# radians = calcular ângulos sen, cos, tang.
# a lista fica []
# from math import sqrt é uma biblioteca
# random.choice escolher um valor ou nome
# import random.shuffle vai embaralha
# apertando ctrl mais espaço aparece a funcionalidade do math
#from math import sqrt = usando esse função não precisar usar raiz, que seria math.sqrt(num)
#pode usar direto raiz = sqrt(num)

#import math

num = int(input('digite um numero:'))
raiz = math.sqrt(num)
#print('A raiz de {} é igual a {}'.format(num, raiz))
#print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
#from math import sqrt floor
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))

