#tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule o seu peso ideial, usando a seguinte fórmula:
#(72.7*altura) -  58

altura = float(input("Digite sua altura em metros (separando por um ponto metros de centímereos): "))
peso_ideial = (72.7 * altura) - 58 
print("Seu peso idela é de", peso_ideial, "kg.")
