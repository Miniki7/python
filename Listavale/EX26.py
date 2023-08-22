'''26) Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres).'''
n = input("Digite seu nome [minimo 3 caracteres]: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
sexo = input("Sexo F para feminino ou M para masculino: ")
print('Estado Civil \n s= solteiro \n c = casado \n separado \n viúvo\n divorciado')
civil = input("Estado civil (s, c, v ou d): ")

while len(n) <= 2:
    n = input("Seu nome deve ter mais que 2 caracteres: ")
    n = input("Digite seu nome [minimo 3 caracteres]: ")
    if len(n) < 2:
        break

while (idade < 0) or (idade > 150):
    idade = int(input("Sua idade deve estar entre 0 e 150 anos: "))

while (salario < 0):
    salario = float(input("Não existe salario negativo "))

while (sexo != 'F') and (sexo !='M'):
    sexo = input("Voce nao escolheu se é do sexo masculino e nem feminino ")

while (civil!='s')and(civil!='c')and(civil!='v')and(civil!='d'):
    print("Voce nao escolheu seu estado civil'")
    civil = input("Estado civil (s, c, v ou d): ")