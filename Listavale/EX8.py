#8) Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
l = float(input('Digite a largura de um predio em metros: '))
a = float(input('Digite a altura de um predio em metros: '))
area = l*a
print(f'A area do predio é {area}')
print(f'A quantidade de tinta nessesaria sera {area/2}')