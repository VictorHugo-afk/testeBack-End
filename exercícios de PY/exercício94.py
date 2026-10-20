from datetime import datetime
dados = {}
dados ['nome'] = str (input('Digite seu nome: '))
nasc = int(input('Em que ano você nasceu? '))
dados ['idade'] = datetime.now ().year - nasc
dados ['ctps'] = int(input('Qual é o seu ctps '))
if dados['ctps'] !=0:
    dados ['contratacao'] = int(input('Ano de contratacao'))
    dados ['salário'] = float(input('Salário: '))
    dados ['aposentadoria'] = ((dados ['contratacao'] + 35) - datetime.now ().year)
for k,v in dados.items():
    print(f'{k} tem o valor {v}')