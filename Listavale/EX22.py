'''22) Crie um programa que leia vários números inteiros pelo teclado. O programa só pode para quando for
digitado o numero 1000. No final, mostre quantos números foram digitados e qual foi a soma deles.
Desconsiderando o valor 1000 da parada.'''
s = 0
q = 0
while True:
   n = int(input("Digite um número inteiro: "))
   if n == 1000:
      break
   s = s + n
   q = q + 1
print(f'A quantidade de números digitados foi: {q}')
print(f'A soma dos numeros digitados foi {s}')
