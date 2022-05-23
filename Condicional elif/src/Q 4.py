num = int(input('Digite um número: '))
if num % 3 == 0 and num % 5 == 0:
    print('É divisivel por 3 e 5')
elif num % 3 == 0:
    print('É divisivel por 3')
elif num % 5 == 0:
    print('É divisivel por 5')
else:
    print('Não divisivel nem por 3 ou 5 ')
