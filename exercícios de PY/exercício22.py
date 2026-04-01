from random import shuffle
Aluno1 = str (input('Primeiro Aluno: '))
Aluno2 = str (input('Segundo Aluno: '))
Aluno3 = str (input('Terceiro Aluno: '))
Aluno4 = str (input('Quarto Aluno: '))
lista = [Aluno1, Aluno2, Aluno3, Aluno4]
shuffle (lista)
print ('A ordem de apresentação será {}' .format(lista))