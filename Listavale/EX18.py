'''18) Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem
peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi
aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos'''
n1 = float(input("Digite a nota da prova 1(maximo 5 pontos): "))
n2 = float(input('Digite a nota da prova 2(maximo 5 pontos): '))
n3 = float(input('Digite a nota da prova 3(maximo 10 pontos): '))
if n1 + n2 > 10 or n1 < 0 or n2 < 0 or n3 > 10 or n3< 0:
    print(f'Nota Invalidas. Você digitou alguma coisa errada. Você digitou essa notas n1 {n1}, N2 {n2} e N3 {n3} ')
else:
    media = (n1+n2+n3)/2
    if media >= 6:
        print(f'O aluno foi APROVADO com media {media}')
    else:
        print('O aluno foi REPROVADO!!')
