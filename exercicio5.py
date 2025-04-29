array = []

print("Quando você quiser finalizar, digite -> -1")
while True:
    x = int(input("Digite um número: "))
    array.append(x)

    if x == -1:
        break

print(f"Seu array final é: {array}")