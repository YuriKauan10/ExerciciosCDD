x = int(input("Digite um número: "))

pares = []
impares = []

for i in range(1, x + 1, 1):
    if i % 2 == 0:
        pares.append(i)
    elif i % 2 != 0:
        impares.append(i)

print(pares)
print(f"{impares}\n")

somaPares = 0
somaImpares = 0

for i in pares:
    somaPares += i

for i in impares:
    somaImpares += i

print(f"Soma dos números pares: {somaPares}")
print(f"Soma dos números impares: {somaImpares}")