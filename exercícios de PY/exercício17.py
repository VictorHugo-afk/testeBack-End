dias = int (input('Quantos dias alugados ?'))
km = float (input('Quantos km rodados ?'))
diaria = dias*60
percurso = km * 0.15
custo = diaria + percurso 

print('O total a pagar é de R${:.2f}' .format(custo))