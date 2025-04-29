a = [""]*5

for i in range(len(a)):
    a[i] = int(input("Digite um número: "))

x = int(input("Digite outro número: "))

m = []

for i in a:
    m.append(i)

for z in range(len(m)):
    m[z] = m[z] * x

print(f"Array digitado: {a}")
print(f"Array multiplicado por {x}: {m}")

