#faça um programa que peça dois números inteiros e um número real. Valcule e mostre:
#o produto do dobro do primeiro com a metade do segundo 
#a soma do triplo do primeiro com metade do segundo
#o terceiro elevado ao cubo

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 =float(input("Digite o número real: "))

resultado1 = (num1 * 2) * (num2 / 2)
resultado2 = (num1 * 3) + (num2 / 2)
resultado3 = num3 ** 3

print ("O produto do dobro do primeiro com a metade do segundo é ", resultado1)
print ("A Soma do triplo do primeiro com a metade do segundo é ", resultado2)
print ("O terceiro elevado ao cubo é ", resultado3)

