usuario = ["joao", "carlos", "mario"]
senha = [1234,3432,5432]

msg = ""
contErro = 0

while True:
    usuarioLogin = input("\nDigite seu usuário para login: ")
    senhaLogin = int(input("Digite sua senha para login: "))

    for i in range(len(usuario)):
        if usuarioLogin == usuario[i] and senhaLogin == senha[i]:
            msg = "Login efetuado"
            break


    if msg == "Login efetuado":
        print(msg)
        break
    else:
        print("Login incorreto")
        contErro += 1
        if contErro == 3:
            print("VOCÊ FOI BLOQUEADO POR EXCESSO DE TENTATIVA!")
            break

        continue




