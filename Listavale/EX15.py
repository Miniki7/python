#15) Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na tela dizendo se está “quente”, “frio” ou “agradável”.
atual = float(input('Digite a temperatura atual:'))
if atual < 20:
    print('A temperatura esta fria')
elif atual > 20 and atual <30:
    print('A temperatura esta agradavel')
else:
    print('A temperatura esta Quente!')