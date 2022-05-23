num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))

if num1 > num2 and num1 > num3:
    print('O número 1 é maior:', num1)
elif num2 > num1 and num2 > num3:
    print('O número 2 é maior:', num2)
elif num3 > num1 and num3 > num2:
    print('O número 3 é maior:', num3)
