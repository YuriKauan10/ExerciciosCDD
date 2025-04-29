array = [""]*5

for i in range(len(array)):
    x = float(input("Digite um número: "))
    array[i] = x

print(f"Array na ordem normal: {array}")

print("Ordem reversa:")
for i in range(len(array)-1, -1, -1):
    print(array[i], end = "")
