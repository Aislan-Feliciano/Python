#o mesmo prof. do desafio anterior quer sorter a ordem da apresentação do trabalho dos alunos. faça
#um programa que leia os nomes dos quatros alunos e mostre as ordem sorteada.
'''from math import shuffle'''
import random
n1 = input('primeiro aluno:')
n2 = input('segundo aluno:')
n3 = input('terceiro aluno:')
n4 = input('quarto aluno:')
lista = [n1, n2, n3, n4]
sorteio = random.shuffle(lista)
print('A ordem de apresentação será {}'.format(lista))