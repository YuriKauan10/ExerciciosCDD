
x = input("Digite uma frase: ")

cont = 0

for i in x:
    if i in "aáãâAÁÂÃ":
        cont += 1

print(f"Sua frase tem {cont} palavras A")
