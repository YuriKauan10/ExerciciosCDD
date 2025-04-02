tipo = input("Digite o tipo do combustivel \n"
             "E - Etanol \n"
             "G- Gasolina : ").upper()
quantidade = float(input("Digite a quantidade de litros abastecidos: "))
valor = 0
if tipo == "E":
    valor = quantidade * 4.90
elif tipo == 'G':
    valor = quantidade * 5.80
else:
    print("Opção invalida")

print(f"Sua quantidade de litros: {quantidade}L")
print(f"Valor a ser pago: R${valor:.2f}")