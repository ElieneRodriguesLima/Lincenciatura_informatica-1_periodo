a = int(input('Diga o valor de A: '))
b = int(input('Diga outro valor B: '))
if a % b == 0:
    print('É multiplo!')
elif b % a == 0:
    print('É multiplo!')
else:
    print('Não é multiplo')