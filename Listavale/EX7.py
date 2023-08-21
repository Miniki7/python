#7) Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15% de aumento.
produto = float(input('Digite o valor do produto: '))#receber o valor do produto
des = produto*0.95
print(f'O preço de um produto com 5% de desconto é {des}') 
aum = produto * 0.15 + produto
print(f'O preço de um produto com 15% de aumento é {aum}') 