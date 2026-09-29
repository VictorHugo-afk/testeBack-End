Ficha = []
while True:
    nome = str(input('Nome: '))
    Nota1 = float(input('Nota1: '))
    Nota2 = float(input('Nota2: '))
    Media = (Nota1 + Nota2)/2
    
    Ficha.append([nome, [Nota1, Nota2], Media])
    Resp = str (input('Quer Continuar? '))
    if Resp in 'Nm':
        break
print(f'{'n':<4} {'Nome':<10} {'Media':>8}')
for i, a in enumerate (Ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        break
    if opc <= len(Ficha)-1:
        print(f'Notas de {Ficha [opc] [0]} são {Ficha [opc] [1]}')