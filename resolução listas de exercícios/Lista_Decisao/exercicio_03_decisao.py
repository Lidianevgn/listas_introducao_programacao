#As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se forem compradas pelo menos 12. 
#Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

qm = int (input ("Quantas maçãs você irá comprar? "))
if qm <12:
    valor = 1.3 
else:
    valor = 1 

custo_compra = qm * valor
print ("O valor total a ser pago pela sua compra é de R$", custo_compra)
