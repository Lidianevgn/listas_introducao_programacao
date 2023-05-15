#Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if valor1 < valor2:
    print("os valores em ordem crescente são: " , valor1, valor2)

else: 
    print("oS valores em ordem crescente são: " , valor2, valor1)