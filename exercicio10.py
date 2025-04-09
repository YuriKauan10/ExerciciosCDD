contDentro = 0
contFora = 0

for i in range(4):
    x = int(input("Digite um número: "))
    if 10 <= x <= 20:
        contDentro += 1
    else:
        contFora += 1

print(f"Números entre [10,20]: {contDentro}")
print(f"Números fora desta condição: {contFora}")