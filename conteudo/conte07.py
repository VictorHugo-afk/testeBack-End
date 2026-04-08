frase = 'Curso de analise de desenvolvimento de sistemas'
print (frase [7]) #Isso mostra o espaço na memória
print (frase [40:45]) #intervalo de caracteres menos o último
print (frase [40:45:2]) #Essa parte pula de dois em dois
print (frase [:7]) #Pega do ínicio até o caractere que você escolheu
print (frase [2:]) #Pega do caractere que você escolheu até o final
print (frase [7::2]) #Pega do caractere escolhido pulando de 3 em 3 
print (len (frase)) #Esse metodo conta a quantidade de caracteres
print (frase.count('s')) #Count procura um caractere específico
print (frase.count('a', 2,10)) #Ele procura quantas letras o número de caractere escolhido até 10 caracteres
print (frase.find ('desen')) #O find mostra a partir de qual indice aprece a pesquisa
print (frase.find ('android')) #O resultado -1 indica que não tem essa sequencia no resultado
print ('analise'in frase) #O in verifica se aquele conjunto está na variavel
print (frase.replace ('analise', 'programação')) #Troca a palavra
print (frase)
print (frase.upper()) #Deixa as letras maiusculas
print (frase.lower()) #Deixa as letras minusculas
print (frase.capitalize()) #Deixa a primeira letra da primeira palavra maiuscula
print (frase.title()) #Deixa a primeira letra das palavras em maisculas
print (frase.strip ()) #Tira espaços
print (frase.rstrip ()) #tirar o espaço do lado esquerdo
print (frase.lstrip ()) #tirar o espaço do lado direito

print (frase.split ()) #Vai transformar o valor da variavel em lista
print ('¨'.join (frase)) #Une um simbolo em cada parte do split