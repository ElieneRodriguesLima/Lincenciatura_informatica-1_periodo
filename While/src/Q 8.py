x = 1
cont = 0
n = int(input('Digite um número par: '))
while x < n:
    x = x + 1
    if x % 2 == 0:
        cont = cont + 1
print(cont)
print('Fim do programa')
