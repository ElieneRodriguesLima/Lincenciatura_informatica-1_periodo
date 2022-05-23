idade = int(input('Idade: '))
sexo = int(input('Sexo (0 = Masculino 1 = Feminino): '))
anos_rest = 0

if sexo == 0:
    anos_rest = 70 - idade
else:
    anos_rest = 65 - idade

if anos_rest > 0:
    print(f'Faltam {anos_rest} anos para você se aposentar')

else:
    print('Você já pode se aposentar')