#tendo como dados de enrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal usando as seguintes fórmulas:
#Para homens: (72.7*h)-58
#Para Mulheres: (62.1*h)-44.7 

genero = input("Qual o seu gênero fisiológico (M para masculino e F para Feminino)? ")
altura = float(input("Qual a sua altura em metros (separe por um ponto metros de centímetros)? "))

if genero == "M":
    peso_ideial = (72.7 * altura) - 58 
    print("Seu peso ideal é de", peso_ideial, "kg.")

elif genero == "F":
    peso_ideial = (62.1 * altura) - 44.7
    print("Seu peso ideal é de", peso_ideial, "kg.")

else:
    print("Gênero não reconhecido. Por favor, tente novamente digirando M para Masculino e F para Feminino.")
