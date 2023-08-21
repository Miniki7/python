'''21) Crie um programa que leia dois valores e mostre na tela um menu :
a. Somar
b. Multiplicar
c. Maior
d. Menor
e. Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso'''
menu = int(input('1. Somar \n' 
'2. Multiplicar \n'
'3. Maior \n'
'4. Menor \n'
'5. Sair do programa: \n'))
if menu == 1:
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite um numero: '))
    print(f'A soma é {n1+n2}') 
elif menu == 2:
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite um numero: '))
    print(f'O produto é {n1*n2}') 
elif menu == 3:
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite um numero: '))
    if n1 > n2:
        print(f'O numeron maior é: {n1}') 
    else:
        print(f'O numeron maior é: {n2}')
elif menu == 4:
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite um numero: '))
    if n1 < n2:
        print(f'O numeron menor é: {n1}') 
    else:
        print(f'O numeron menor é: {n2}')
else:
   print('Você saiu do programa')