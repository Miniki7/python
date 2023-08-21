'''20) Leia a idade e o tempo de servico de um trabalhador e escreva se ele pode ou nao se aposentar.
As condições para aposentadoria são:
• Ter pelo menos 65 anos,
• Ou ter trabalhado pelo menos 30 anos,
• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos'''
idade = int(input('Digite sua idade: '))
tservi = int(input('Digite seu tempo de ser: '))#tservi = tempo serviço
if idade > 64 or tservi > 29 or (idade >=60 and tservi >=25):
    print('O trabalhador pode se aposentar!')
else:
    print('O trabalhador NÃO pode se aposentar!')