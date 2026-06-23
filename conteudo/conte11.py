#c = 1
#while c < 10:
#    print(c)
#    c += 1

# n = 1
# while n != 0:
#     n = int(input ('Digite um valor:'))
# print('Fim')

# r = ('sim')
# while r == 'sim':
#     n = int(input('digite um valor'))
#     r = str(input('quer continuar? [sim/não]:')).lower()
#print('fim')

n = 1
par = 0 
ímpar = 0 
while n != 0:
    n = int(input('digite um valor: '))
    if n % 2 == 0:
        par +=1
    else:
        ímpar +=1
print('você digitou {par} números pares e {ímpar} números ímpares')