#num = int(input('Digite um número entre 0 e 9999: '))
#unidade = num % 10
#centena = (num // 100) % 10
#print(f'Unidade: {unidade}')
#print(f'Centena: {centena}')

#nome_completo = input("Digite o nome completo: ").strip()
#nomes = nome_completo.split()
#if len(nomes) > 1:
#    segundo_nome = nomes[1]
#    quantidade_letras = len(segundo_nome)
#    print(f"O segundo nome é '{segundo_nome}' e ele tem {quantidade_letras} letras.")
#else:
#    print("Você digitou apenas um nome. Não foi possível encontrar o segundo.")

#frase = "estou fazendo uma prova de backend"
#frase_modificada = frase.replace(" ", "*")
#print(frase_modificada)

# texto = "O aprendizado constante é a chave para o sucesso."
# palavra_procurada = "chave"

# posicao = texto.find(palavra_procurada)

# print(f"A posição da palavra é: {posicao}")

# print('='*30)
# print('BANCO CEV')
# print('='*30)
# valor = int(input('Que valor você quer sacar? R$ '))
# total = valor
# ced = 100
# totalced = 0
# while True:
#     if total >= ced:
#         total -= ced
#         totalced += 1
#     else:
#         if totalced > 0:
#             print(f'Total de {totalced} cédulas de R${ced}')
#         if ced == 100:
#             ced = 50
#         elif ced == 50:
#             ced = 5
#         elif ced == 5:
#             ced = 2
#         elif ced == 2:
#             ced = 1
#         totalced = 0
#         if total == 0:
#             break
# print('='*30)
# print('VOLTE SEMPRE')

n = 0
c = 0
multipli = 1
q = 0
s = 0
while True:
    n = int(input('Digite um número [757 para parar]: '))
    c += 1
    s += n
    if n == 757:
        multipli *= n 
        q += 1
    
        break
    multipli *= n
    q += 1
    

print(f'A quantidade de números digitados foram {q} ')
print(f'A multiplicação de todos incluindo o flag deu {multipli} ')