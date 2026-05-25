#n1 = float(input("Digite a primeira nota: "))
#n2 = float(input("Digite a segunda nota: "))
#m = (n1 + n2) / 2
#print("A sua média foi {:.1f}".format(m))

#if m >= 6.0:
    #print("A sua média foi boa! Parabéns")
#else:
    #print("Sua média foi ruim! Estude mais")

#print("Parabéns" if m >= 6 else "Estude mais")

#for c in range(0,6): #desconsidera o último
#    print("oi")
#print("FIM")

#for c in range(0,6):
#    print(c)
#print("FIM")

#for c in range(6,0,-1): # o -1 faz ele contar em forma decrescente
#    print(c)
#print("FIM")

#for c in range(0,6,2): # ele pula de 2 em 2
#    print(c)
#print("FIM")


#n = int(input("Digite um número: "))
#for c in range(0, n+1):
 #   print(c)
#print("FIM")
#i = int(input("Início: "))
#f = int(input("Fim: "))
#p = int(input("Passo: "))
#for c in range(i, f+1, p):
#    print(c)
#print("FIM")

s = 0
for c in range(0, 4):
    n = int(input("Digite um valor: "))
    s += n #s = s + n
print(f"O somatório de todos os valores foi {s}")