vlc = float(input('Diga qual velocidade você percorreu?: '))
multa = 0
vlc_km = 0

if vlc > 80:
    multa = (vlc - 80) * 5
    print(f'Você será multado em  R$ {multa:.2f}')
if vlc <= 80:
    print('Parabéns você dirige com atenção e não será multado!')

print('Fim de programa!')
