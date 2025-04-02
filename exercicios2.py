quantidade = int(input("Digite seu número: "))

for i in range(1, quantidade + 1):
    # Calcula o número de espaços necessários para centralizar
    espaços = quantidade - i
    # Cria uma linha com os asteriscos separados por espaço
    linha = " ".join("*" * i)
    # Imprime os espaços seguidos da linha com asteriscos
    print(" " * espaços + linha)