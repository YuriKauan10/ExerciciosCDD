usuario = [""] * 2
senha = [""] * 2

for i in range(len(usuario)):
    usuario[i] = input("Digite o usuário para cadastro: ")
    senha[i] = int(input("Digite sua senha para cadastro: "))

usuarioLogin = input("Digite seu usuário para login: ")
senhaLogin = int(input("Digite sua senha para login: "))

login_sucesso = False

for i in range(len(usuario)):
    if usuarioLogin == usuario[i] and senhaLogin == senha[i]:
        login_sucesso = True
        break
if login_sucesso:
    print("Login efetuado com sucesso")
else:
    print("Login incorreto")

