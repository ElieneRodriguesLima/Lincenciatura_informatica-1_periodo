x = int(input('Digite um número: '))
impar = 0
while impar < 6:
    x = x + 1
    impar += 1
    if x % 2 != 0:
        print(f'{x}')
