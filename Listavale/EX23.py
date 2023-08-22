'''23) Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os
valores lidos e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou
não continuar a escrever valores.'''
s = 0
q = 0
maior = 0
menor = 1000
while True:
   n = int(input("Digite um número inteiro: "))
   if n == 1000:
      break
   s = s + n
   q = q + 1
   if n > maior:
      maior = n
   elif n < menor:
      menor = n
print(f'A media dos números digitados foi {s/q}')
print(f'O maior numero digitado foi {maior} e o menor {menor}')