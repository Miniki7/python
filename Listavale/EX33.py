'''33) Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os
códigos utilizados são:
 1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
a. O total de votos para cada candidato;
b. O total de votos nulos;
c. O total de votos em branco;
d. A percentagem de votos nulos sobre o total de votos;
e. A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o
valor zero.'''
def main():
    candidatos = {
        1: "Jose",
        2: "João",
        3: "Maria",
        4: "Ana"
    }
    
    total_votos_candidatos = {candidato: 0 for candidato in candidatos.values()}
    total_votos_nulos = 0
    total_votos_brancos = 0
    total_votos = 0
    
    while True:
        voto = int(input("Informe o código do voto (ou 0 para encerrar): "))
        
        if voto == 0:
            break
        
        if voto in candidatos:
            total_votos_candidatos[candidatos[voto]] += 1
        elif voto == 5:
            total_votos_nulos += 1
        elif voto == 6:
            total_votos_brancos += 1
        
        total_votos += 1
    
    percentual_nulos = (total_votos_nulos / total_votos) * 100
    percentual_brancos = (total_votos_brancos / total_votos) * 100
    
    print("\nResultado da Eleição:")
    for candidato, votos in total_votos_candidatos.items():
        print(f"{candidato}: {votos} votos")
    
    print(f"Votos Nulos: {total_votos_nulos}")
    print(f"Votos em Branco: {total_votos_brancos}")
    print(f"Percentual de Votos Nulos: {percentual_nulos:.2f}%")
    print(f"Percentual de Votos em Branco: {percentual_brancos:.2f}%")
    print(f"Total de Votos: {total_votos}")

if __name__ == "__main__":
    main()
