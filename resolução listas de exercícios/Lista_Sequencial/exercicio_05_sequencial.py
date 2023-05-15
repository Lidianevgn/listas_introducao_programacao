#faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. 
#c = 5 *((F-32) /9)

fahrenheit = float(input("Qual a temperatura em graus Fahrenheit? "))
celsius = 5 * (fahrenheit - 32) / 9
print(fahrenheit, "graus Fahrenheit é igual a", celsius, "graus Celsius")
