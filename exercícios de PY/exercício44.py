print("-=-" * 10)
print("Analisador de Triângulos")
print("-=-" * 10)

# Atribuição das variáveis
a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

# Verificação da existência do triângulo e classificação
if a < b + c and b < a + c and c < a + b:
    print("Os segmentos acima podem formar um triângulo ", end="")
    if a == b == c:
        print("EQUILÁTERO")
    elif a != b and a != c and b != c:
        print("ESCALENO")
    else:
        print("ISÓSCELES")
else:
    print("Os segmentos acima NÃO PODEM formar um triângulo.")
