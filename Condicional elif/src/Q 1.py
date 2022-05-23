nota = float(input('Digite sua nota: '))
if 6 <= nota and nota <=10:
    print('Você está aprovado')
elif 0 <= nota and nota < 6:
    print('Você está reprovado')
else:
    print('Nota Inválida')