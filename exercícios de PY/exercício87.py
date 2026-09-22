Valores = []
Temp = []
Impar = []
Par = []

for c in range (0,7):
    Temp.append (int(input ('Digite um número ')))
    Valores.append (Temp[:])
    if Temp[0] % 2 == 0:
        Par.append (Temp[:])
    else:
        Impar.append (Temp[:])
    Temp.clear()
    Impar.sort()
    Par.sort()
print(f'Os valores pares em ordem crescente são {Par}, e os ímapares são {Impar}')