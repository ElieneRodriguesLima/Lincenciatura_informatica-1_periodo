dist = float(input('Diga sua distância: '))
if dist <= 200:
    passagem = 0.50 * dist
else:
    passagem = 0.45 * dist
print(f'O preço de sua passagem será de = R${passagem:.2f}')