imp_renda = 0
inss = 0
slr_final = 0

slr_func = float(input('Diga qual é seu salário: '))
if slr_func < 1000:
    imp_renda = 0 * slr_func
    inss = 0 * slr_func
    slr_final = slr_func
    print(f'Você não pagará imposto e nem pagará inss!')

if slr_func >= 1000:
    if slr_func < 2000:
        imp_renda = 0.10 * slr_func
        inss = 0.11 * slr_func
        slr_final = slr_func - imp_renda - inss
        print(f'Você Será cobrado\nIMPOSTO DE RENDA = R${imp_renda:.2f}\nINSS = R${inss:.2f}\nSALÁRIO TOTAL = R${slr_final:.2f}')

if slr_func >= 2000:
    if slr_func < 3000:
        imp_renda = 0.20 * slr_func
        inss = 0.15 * slr_func
        slr_final = slr_func - imp_renda - inss
        print(f'Você Será cobrado\nIMPOSTO DE RENDA = R${imp_renda:.2f}\nINSS = R${inss:.2f}\nSALÁRIO TOTAL = R${slr_final:.2f}')

if slr_func >= 3000:
    imp_renda = 0.27 * slr_func
    inss = 0.20 * slr_func
    slr_final = slr_func - imp_renda - inss
    print(f'Você Será cobrado\nIMPOSTO DE RENDA = R${imp_renda:.2f}\nINSS = R${inss:.2f}\nSALÁRIO TOTAL = R${slr_final:.2f}')

