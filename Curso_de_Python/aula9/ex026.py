'''Faça um progrma que leia uma frase pelo teclado e mostre:
Quantas vezes mostra a letra A:
Em que posição ela aparece a primeira vez:
Em que posição ela aparece pela ultima vez:'''

frase = str(input('didite uma frase:')).upper().strip()
n1 = frase.find('A') + 1
n2 = frase.rfind('A') + 1
 # Vai colacar + 1 porque o programa python começa com o numero '0', eu quero que comece o numero '1'
print('A analisando a frase {}'.format(frase))
print('A letra A apareceu na posição {}'.format(n1))
print('A letr A apareceu na posição {}'.format(n2))