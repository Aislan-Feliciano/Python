'''print(frase.upper().count('O')) 'upper' vai pegar a frase colocar a letra 'O' em maiuscula; 'count'
vai contar quantas letras 'O' tem.'''

'''frase = ('curso em video python')
print(frase[2:]), vai começar da letra 'r' ate o final da frase;
frase[:2] vai da letra 'c' ate a letar 'u'; '''

'''frase = ('curso em video python')'count' vai contar quantas letras 'o' tem
print(frase.count('o')); se colocar frase.count(' ') com espaço dentro do parentese sem nada é uma
varável; '''

'''frase = ('curso em video python') 'upper' vai transformar as letras para maiusculas, utlizando
upper().count(), vai contar todas as letras maiusculuas.
print(frase.upper().count())'''

'''frase = ('curso em video python')'len' vai ver o tamanho da frase, se eu colocar strip
 remove os espaço indesejados na frase len(frase.strip())
print(len(frase))'''

'''frase = ('curso em video python') 'replace' vai trocar algum nome da frase por outro
n1 = frase.replace('python','android')
print(n1)'''

'''frase = ('curso em video python') 'in' vai mostrar se a palavra esta dentro frase
print('curso' in frase)'''

'''frase = ('Curso em Video Python') 'find' significar encontrar. 'lower' substitui todas as letras
maiusculas para minusculas
print(frase.lower().find('video'))'''

'''frase = ('curso em video python')'split' vai criar uma divisão entre os espaços
print(frase.split())'''

'''frase = ('curso em video python')
divido = frase.split()
print(divido[0][3])'''

'''nome = str(input('Qual é seu nome completo?'))
separação = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separação[0], len(separação[0])))'''

nome = str(input('Qual é seu nome completo?'))
print('seu nome todo tem {} letras'.format(len( nome.strip(' nome'))))