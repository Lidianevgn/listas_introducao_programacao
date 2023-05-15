# Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após,
#calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também
#testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo',
#senão escrever a mensagem 'Saldo Negativo'.

nc = int(input("Digite o número da conta: "))
s = float(input("Digite o saldo: "))
d = float(input("Digite o débito: "))
c = float(input("Digite o crédito: "))

sa = s - d + c
print("Saldo Atual é R$ {:.2f}".format(sa))
if sa >= 0:
    print("Saldo Positivo")
else:
    print("Saldo negativo")



