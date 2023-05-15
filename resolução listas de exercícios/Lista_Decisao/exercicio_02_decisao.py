#Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou
#negativo (considere o valor zero como positivo).

num = float (input("Digite um valor numérico inteiro ou real: "))
if num >= 0:
    print ("O valor digitado é positivo!")
elif num < 0: 
    print ("O valor digitado é negativo!")
    