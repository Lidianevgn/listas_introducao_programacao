#Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou menor que 10. 
#O programa deve escrever a mensagem correspondente (maior ou menor) e informar o valor digitado pelo usuário.

valor = float (input ("Digite um valor numérico: "))
if valor >10:
    print("o valor é maior que 10!")
elif valor <10: 
    print("o valor é menor que 10!")
else:
    print("o valor é igual a 10")