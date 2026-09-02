# Podemos adicionar uma lista dentri de outra lista. Para isso utilizamos a sintaxe nome da lista. append(nome da outra lista [:]), cada lista adicionada vira um elemento dentro da lista externa. Podemos declarar de forma direta igualando a lista externa as listas que eu quero adicionar colocando os dados entre colchetes e separando cada conjunto de lista por vírgula. Ex pessoas = [['pedro', 75], ['maria, 19], ['joao',32]]. O indices de cada lista são 0, 1, 2 respectivamente.

# Listas parte 2
# Para mostrar-mos um item dentro de uma lista interna primeiro colocamos o índice da lista depois o índice do item dentro da lista. Ex print(pessoas[0][0]) irá mostrar 'pedro', print (pessoas[1][1] vai aparecer 19, print(pessoas [2][0]) vai aparecer joão, print(pessoas[1]) vai aparecer ['maria', 19]

Teste = []
Teste.append ('Victor')
Teste.append (19)
Galera = []
# Galera.append (Teste)
Galera.append (Teste [:])
Teste [0] = 'Maria'
Teste [1] = 22
Galera.append (Teste [:])



print (Teste)
print (Galera)