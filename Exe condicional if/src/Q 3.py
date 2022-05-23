amt = 0
slr_func = float(input('Digite seu salário: '))
if slr_func > 1250:
    amt = 0.10 * slr_func

if slr_func <= 1250:
    amt = 0.15 * slr_func

print(f'Seu aumento de salário será de R$ {amt:.2f}')
