'''Escreva um programa que pergunte o salário de funcionário e calcule o valor de seu aumento.
Para o salário superiores R$ 1.250. Calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Quanto você ganha mensalmente?'))
n1 = (salario * 10) /100
n2 = (salario * 15) /100
if salario > 1250:
    print('o salario for maior {:.2f}, teve um aumento de {:.2f}.'.format(salario, n1))
if salario < 1250:
        print('Se o salario for menor que {:.2f}, teve um aumento de {:.2f}.'.format(salario, n2))
