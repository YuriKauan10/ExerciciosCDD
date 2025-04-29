nomes = [""]*5

i = 0

while True:
    nomepedido = str(input("Digite um nome: "))
    nomes.insert(i, nomepedido)
    i += 1

    for i2 in nomes:
        if i2 == "":
            nomes.pop()
    if i == 5:
        print(nomes)
        break
