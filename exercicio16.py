usuario = ["joao", "carlos", "mario"]
senha = [1234,3432,5432]

usuarioLogin = input("Digite seu usuário para login: ")
senhaLogin = int(input("Digite sua senha para login: "))


msg = ""

for i in range(len(usuario)):
    if usuarioLogin == usuario[i] and senhaLogin == senha[i]:
        msg = "Login efetuado"
        break

if msg == "Login efetuado":
    print(msg)
else:
    print("Login incorreto")

