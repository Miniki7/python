'''27) Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120'''
n = int(input('Digite um número inteiro: '))
c = n
f = 1
while c != 1:
    f = f * c
    c -= 1
    print ('{} x {} = {}'.format(n,c,f))
print (f'O valor fatorial de {n} é igual a {f}!')