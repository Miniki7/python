#11) Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E ao final mostrar seu nome e salário final calculado
nome = input('Digite seu nome: ')
horas = int(input('Digite o numero de horas trabalhadas: '))
valor = float(input('Digite o valor da hora trabalhada: '))
salario = horas * valor
des = salario * 0.98
print('Informacoes do funcionario: \n nome: {nome} \n seu salario final é: {des}')