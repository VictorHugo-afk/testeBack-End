import math
ang = float (input('Qual é o ângulo? '))
cose = math.acosh (math.radians(ang))
seno = math.asinh (math.radians(ang))
tang = math.atanh (math.radians(ang))
print('O ângulo de {} tem cose de {:.2f}' .format(cose))
print('O ângulo de {} tem seno de {:.2f}' .format(seno))
print('O ângulo de {} tem tang de {:.2f}' .format(tang))