#Faça um script que leia dois números e retorne como resultado a soma deles. Faça um script que leia algo pelo teclado e mostra na tela o seu tipo de dado
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))
print(f'A soma de {n1} e {n2} é {n1+n2}')
script = input('Digite algo pelo teclado: ')
print(f'O tipo de dado é {type(script)}')