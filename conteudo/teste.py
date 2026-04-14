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

texto = "O aprendizado constante é a chave para o sucesso."
palavra_procurada = "chave"

posicao = texto.find(palavra_procurada)

print(f"A posição da palavra é: {posicao}")

