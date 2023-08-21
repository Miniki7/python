#16) Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida conversão.
print('FAhrenheit p/ Celsius = F')
print('Celsius p/ FAhrenheit = C')
decidir = input('Digite para qual temperatura gostaria de passar (F ou C): ')
if decidir == 'F':
    F = float(input('Digite o valor em Fahrenheit: '))
    passar = (F - 32)/1.8
    print(f'A temperatura {F} de Fahrenheit para Celsius é {passar}')
else: 
    C = float(input('Digite o valor em Celsius: '))
    passar = C * 1.8 + 32
    print(f'A temperatura {C} de Celsius para Fahrenheit é {passar}')