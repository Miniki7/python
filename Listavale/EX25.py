'''25) Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do
usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''
n = input('Digite seu nome: ')
s = input('Digite sua senha: ')
while s == n:
    print("ERROR")
    print("ERROR")
    print("ERROR")
    s = input('Digite sua senha: ')
    if s != n:
        break