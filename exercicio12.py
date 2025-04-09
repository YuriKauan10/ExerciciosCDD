array = []

for i in range(5):
    x = float(input("Digite um número:"))
    array.append(x)

soma = 0
quantidade = 0

for i, v in enumerate(array):
    soma += v
    if i >= 0:
        quantidade += 1

res = soma / quantidade
print(res)
