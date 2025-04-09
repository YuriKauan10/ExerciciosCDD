
valores = []

for i in range(1, 11, 1):
    x = int(input("Digite um número: "))
    valores.append(x)

print("---------------------")

quantidade = 0

for i in valores:

    if i < 0:
        quantidade += 1


print(f"{quantidade} números são negativos.")