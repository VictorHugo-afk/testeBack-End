nome = input ('Qual é o seu nome?')
print ('prazer em conhece-lo {:20}!' .format(nome))
print ('prazer em conhece-lo {:>20}!' .format(nome)) # Maior é para direita
print ('prazer em conhece-lo {:<20}!' .format(nome)) # Menor é para esquerda
print ('prazer em conhece-lo {:^20}!' .format(nome)) # Alinhamento no centro

num = int (input ('Digite um valor'))
num02 = int (input ('Digite outro valor'))
soma = num+num02  # criar a variavel para utilizar em outro código 
print ('A soma é {}' .format(soma))