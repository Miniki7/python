#6) Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere: US$ 1.00 = R$ 5.41
real = float(input('Digite quantidade de dinheiro que tem na carteira: R$'))
dolar = real/ 5.41
print(f'O valor R${real} em dolars é {dolar}') 