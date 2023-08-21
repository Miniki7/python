#Faça 4 listas:
#A. Filmes
#B. Jogos
#C. Livros
#D. Esporte
#a. Adicione no mínimo 2 itens em cada lista.
#b. Crie uma lista das 4 listas criadas acima.
#c. Acesse (mostrar) algum item da lista livros.
#d. Remova um item da lista esporte.
filmes = ['gato de botas 2', 'os suspeitos', 'o pior vizinho do mundo',' Coisas que Eu Odeio em Você', 'elementos']
jogos = ['Fortnite', 'Valorant', 'World of Warcraft', 'Free Fire', 'Roblox']
livros = ['O Pequeno Príncipe', 'Romeu e Julieta', '1984', 'A Cabana', 'o Senhor dos Anéis']
esporte = ['Atletismo', 'Badminton', 'Baseball', 'Basquete', 'futebol']
#a
filmes.insert(5, 'Cidadão Kane')
filmes.insert(5, 'O Mágico de Oz')

jogos.insert(5, 'Pokémon')
jogos.insert(5, '8 Ball Pool')

livros.insert(5, 'O Retrato de Dorian Gray')
livros.insert(5, 'O Vermelho e o Negro')

esporte.insert(5, 'Voleibo')
esporte.insert(5, 'boxe')
#b
lista = [filmes, jogos, livros, esporte]
print(lista)

#c
print(livros[3])

#d
esporte.pop(3)
print(esporte)