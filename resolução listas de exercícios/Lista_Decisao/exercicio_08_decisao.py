#Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em
#estoque e quantidade mínima em estoque de um produto. Calcular e escrever a
#quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2).
#Se a quantidade em estoque for maior ou igual a quantidade média, escrever a
#mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.

quantidade_atual = int(input("Digite a quantidade atual do seu estoque: "))
quantidade_maxima = int(input("Digite a quantidade máxima do seu estoque:"))
quantidade_minima = int(input("Digite a quantidade mínima do seu estoque:"))

quantidade_media = (quantidade_maxima + quantidade_minima)/2

if quantidade_atual >= quantidade_media:
    print("Não efetuar novas compras")
else: 
    print("Está na hota de efetuar novas compras")
