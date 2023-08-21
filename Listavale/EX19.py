'''19) Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida.
Escreva uma mensagem de erro se a opção for inválida. Escolha a opção:
a. Soma de 2 numeros.
b. Diferença entre 2 números (maior pelo menor).
c.Produto entre 2 números.
d. Divisão entre 2 números (o denominador não pode ser zero).'''

menu = int(input('1. Soma de 2 numeros.\n'
'2. Diferença entre 2 números (maior pelo menor).\n'
'3.Produto entre 2 números.\n'
'4. Divisão entre 2 números (o denominador não pode ser zero). \n'))

if menu == 1:
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite um numero: '))
    print(f'A soma é {n1+n2}') 
elif menu == 2:
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite um numero: '))
    print(f'A subtração é {n1-n2}') 
elif menu == 3:
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite um numero: '))
    print(f'O produto é {n1*n2}') 
elif menu == 4:
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite um numero: '))
    print(f'A soma de {n1/n2}') 
else:
   print('Opção invalida!')