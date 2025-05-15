
arrayNomes = []
for i in range(5):
    x = input("Digite um nome: ")
    arrayNomes.append(x)

print("---------")
print("Nomes que começam com A: ")
for i in range(0, len(arrayNomes)):
    x = arrayNomes[i]
    if x[0] in 'aáâAÁÂ':
        print(arrayNomes[i])



