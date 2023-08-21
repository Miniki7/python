#9) Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para Euros.
n = input('Digite o seu nome: ')
real = float(input('Digite o valor em reais: '))
dolar = real/ 4.99
euro = real/ 5.43
print(f'O valor convertido para Dólar é {dolar} \n o valor convertido para Euros é {euro}')