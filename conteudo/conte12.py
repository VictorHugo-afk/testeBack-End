# conte = 1
# while True:
#     print(conte, '->', end = "")
#     conte += 1
# print('Acabou')

n = s = 0
while True:
    n = int(input('digite um número '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')