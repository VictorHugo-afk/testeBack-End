lista = []
par = []
impar = []

while True:
    num = int(input("Digite um valor: "))
    lista.append(num)
    
    # Separação de pares e ímpares
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
        
    # Pergunta se deseja continuar
    continuar = input('Quer continuar? [S/N] ').strip().lower()
    
    # Se a resposta não começar com 's', encerra o loop
    if not continuar.startswith('s'):
        break

print(f'Os valores digitados foram {lista}, sendo os números {par} pares e os números {impar} ímpares.')
