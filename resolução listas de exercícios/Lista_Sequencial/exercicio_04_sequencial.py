#faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas por mês.
#calcule e mostre o total do seu salário no referido mês. 

valor_hora = float(input("Qual o valor recebido por hora? "))
horas_mes = float(input("Quantas horas são trabalhadas por mês? "))

salario = valor_hora * horas_mes
print("Seu salário mensal é de R$", salario)
