# Inicializa a matriz 3x3 preenchida com zeros
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
total3 = maior = somapar = 0

# Leitura dos dados e processamento
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        
        # A) Soma de todos os valores pares digitados
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
            
        # B) Soma dos valores da terceira coluna (coluna de índice 2)
        if c == 2:
            total3 += matriz[l][c]
            
        # C) Maior valor da segunda linha (linha de índice 1)
        if l == 1 and c == 0:
            maior = matriz[l][c]
        elif l == 1 and c != 0 and matriz[l][c] > maior:
            maior = matriz[l][c]

# Exibição da matriz na tela de forma organizada
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()

# Exibição dos resultados estatísticos
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos números da terceira coluna é igual a {total3}')
print(f'O maior valor da linha 2 é {maior}')