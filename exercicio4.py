numero = int(input("Digite um número para calcular sua fatorial: "))

conta = numero
print(numero, end = "")
for i in range(numero - 1, 0, -1):
    conta *= i
    print(f" * {i}", end = "")

print(f"= {conta}")

