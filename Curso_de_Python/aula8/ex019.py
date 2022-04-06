#um professo quer sortea um dos seus quatros alunos para apagar o quatro. faça um programa que ajude ele
#lendo os nomes deles e escrevendo o nome escolhido.

'''from random import choice'''
import random
n1 = str(input('primeiro aluno:'))
n2 = str(input('segundo aluno:'))
n3 = str(input('terceiro aluno:'))
n4 = str(input('quarto aluno:'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O nome escolhido foi {}'.format(escolhido))
