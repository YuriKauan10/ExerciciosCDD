nomes = ["joao","maria","yuri","carlos","marta"]

pedido = input("Digite um nome para encontrar: ")

for i in range(len(nomes)):
    if nomes[i] == pedido:
        print(f"Nome {pedido} encontrado no índice {i}")
        break

