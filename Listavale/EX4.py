#4) Faça um programa que leia algo pelo teclado e mostre na tela seu tipo de dado e todas as informações sobre ele.
n = input('Digite algo pelo teclado: ')
print(f'O tipo de dado é {type(n)}')
print(n.isnumeric()) #verifica se é numérico
print (n.isalpha()) #verifica se é letra
print(n.isspace()) #se é só espaço
print(n.isalnum()) # se é alpha numerico por exemplo 3a
print(n.isupper()) # se esta em letras maiusculas
print(n.islower()) # se esta em letras minuscula
print(n.istitle()) # palavra capitalizada por exemplo, Python
print(n.capitalize())
print(n.isupper())