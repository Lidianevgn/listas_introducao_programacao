# Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples
# e escrever uma mensagem que diga se o aluno foi ou não aprovado 
# (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

nota1 = float (input("Digite a nota da primeira prova: "))
nota2 = float (input("Digite a nota da segunda prova: "))

media =(nota1 + nota2)/2

print ("A média do aluno é:",  media)

if media >=6:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
    
