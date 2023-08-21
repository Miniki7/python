#12) Escreve um Programa que leia uma lista com no minino 5 itens, contendo itens repetidos e mostreos itens repetidos. 
frutas = ['laranja', 'banana', 'maçã', 'morango', 'uva', 'pera', 'maçã', 'limão', 'banana', 'laranja']
valores = []
repetidos = set()

for frutas in frutas:
    if frutas not in valores:
        valores.append(frutas)
    else:
        repetidos.add(frutas)
print(f'Valores = {valores}')
print(f'Repetidos = {repetidos}')