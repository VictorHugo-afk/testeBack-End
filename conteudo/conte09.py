nome = str(input('Qual é o seu nome? '))
if nome == 'Victor Hugo':
    print('Que nome Bonito!')
elif nome == 'Paulo' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem normal no Brasil')  
elif nome in 'Ana Claudia Jessica Juliana':
    print('Que belo nome feminino')    
else:
    print('Seu nome é bem normal') 
print('Tenha um bom dia {}'.format(nome)) 