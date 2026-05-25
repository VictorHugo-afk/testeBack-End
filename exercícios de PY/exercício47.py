from random import randint
from time import sleep

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogada = int(input("Qual é a sua jogada? "))
jogadapc = randint(0, 2)
itens = ("Pedra", "Papel", "Tesoura")

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO !!!")
sleep(1)

print("-=" * 10)
print(f"O computador jogou {itens[jogadapc]}")
print(f"O jogador jogou {itens[jogada]}")
print("-=" * 10)

if jogadapc == 0:  # Computador jogou PEDRA
    if jogada == 0:
        print("EMPATE")
    elif jogada == 1:
        print("JOGADOR VENCE")
    elif jogada == 2:
        print("COMPUTADOR VENCE")
        
elif jogadapc == 1: # Computador jogou PAPEL
    if jogada == 0:
        print("COMPUTADOR VENCE")
    elif jogada == 1:
        print("EMPATE")
    elif jogada == 2:
        print("JOGADOR VENCE")

elif jogadapc == 2: # Computador jogou TESOURA
    if jogada == 0:
        print("JOGADOR VENCE")
    elif jogada == 1:
        print("COMPUTADOR VENCE")
    elif jogada == 2:
        print("EMPATE")
