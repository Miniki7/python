'''17) Fac¸a um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes formulas (onde h corresponde à altura):
• Homens: (72.7 ∗ h) − 58
• Mulheres: (62, 1 ∗ h) − 44, 7'''
altura = float(input('Digite sua altura: '))
sexo = input('Digite seu sexo:(F ou M) ')
if sexo == "M":
    MMC = (72.7*altura) - 58
    print(f'O seu peso ideal, de acordo com seu sexo é {MMC:.2f}')
else:
    MMC = (62.1 * altura) - 44.7
    print(f'O seu peso ideal, de acordo com seu sexo é {MMC:.2f}')