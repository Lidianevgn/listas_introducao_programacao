#crie uma lidta de convidados para um jantar em sua casa, com pelo menos 5 celebriddes 
#Envie um convite para cada uma dessas pessoas. Como a mesma mensagem e nome personalizado
#Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos convites. imprima o nome das pessoas que não podeão comparecer
#Modifique sua lista, substitua os desistentes por novos convidados
#Exiba um novo convite para cada pessoa que continua presente em sua lista

convidados = ["Elon Musk", "Mark Zuckerberg", "Tim Cook", "Sundar Pichai", "Susan Wojvicki"]
for convidado in convidados: 
    print("Olá", convidado + ", você é uma das pessoas especiais convidadas para um super jantar temático na minha casa, no próximo sábado!")

convidado_desistente = "Tim Cook"
print(convidado_desistente, "não poderá comparecer ao jantar temático.")

convidados.remove(convidado_desistente)
convidados.append("Radia Perlman")

for convidado in convidados:
    print("Olá", convidado + ",  você é uma das pessoas especiais convidadas para um super jantar temático na minha casa, no próximo sábado!")
    print("Infelizmente, os seguintes convidados não poderão comparecer: ")
    print(convidado_desistente)
